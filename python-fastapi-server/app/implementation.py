"""basket API implementation
"""
from datetime import datetime
from fastapi import HTTPException
from .models import SlotValidationNumericRequest, SlotValidationFiniteValuesRequest, SlotValidationResult

class Implementation():
    # get_time -- Synchronisation point for meld
    @staticmethod
    def get_time(*args, **kwargs):
        """
        :param request: An HttpRequest
        """
        return datetime.now().isoformat()

    @staticmethod
    def validate_numeric_entity(body: SlotValidationNumericRequest = None, *args, **kwargs):
        """
        Problem Statement:
        Validate an entity on the basis of its value extracted.
        The method will check if that value satisfies the numeric numerics put on it.
        If there are no numeric numerics, it will simply assume the value is valid.
    
        If there are numeric numerics, then it will only consider a value valid if it satisfies the numeric numerics.
        In case of multiple values being extracted and the support_multiple flag being set to true, the extracted values
        will be filtered so that only those values are used to fill the slot which satisfy the numeric numeric.
    
        If multiple values are supported and even 1 value does not satisfy the numeric numeric, the slot is assumed to be
        partially filled.
    
        :param pick_first: Set to true if the first value is to be picked up
        :param support_multiple: Set to true if multiple utterances of an entity are supported
        :param values: Values extracted by NLU
        :param invalid_trigger: Trigger to use if the extracted value is not supported
        :param key: Dict key to use in the params returned
        :param numeric: Conditional expression for numerics on the numeric values extracted
        :param var_name: Name of the var used to express the numeric numeric
        :return: a tuple of (filled, partially_filled, trigger, params)    
        ...
        filled : True if all values are valid
        partially_filled:
            True when a subset of values are valid
            True when there are values and none of them are valid
        """

        trigger = "" if body.values else body.invalid_trigger 
        valid_values = []
        if body.pick_first and body.values:
            value = body.values[0]
            if body.constraint and not eval(body.constraint, {}, {body.var_name: int(value.value)}):
                    trigger = body.invalid_trigger
            else:
                valid_values = int(value.value)
        elif body.support_multiple:
            for value in body.values:
                if body.constraint and not eval(body.constraint, {}, {body.var_name: int(value.value)}):
                    trigger = body.invalid_trigger
                else:
                    valid_values.append(int(value.value))
        else:
            raise HTTPException(status_code=400, detail="pick_first and support_multiple cannot be both true")

        partially_filled = (bool(valid_values) and bool(trigger)) or (bool(body.values) and not bool(valid_values))
        filled = bool(valid_values) and not bool(trigger)
        parameters = {body.key: valid_values} if valid_values else {}
        return dict( 
            filled=filled, 
            partially_filled=partially_filled,
            trigger=trigger,
            parameters=parameters) 

    @staticmethod 
    def validate_finite_values_entity( body: SlotValidationFiniteValuesRequest = None,
) -> SlotValidationResult:
        """
        Problem Statement:
        Validate an entity on the basis of its value extracted.
        The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").
  
        :param pick_first: Set to true if the first value is to be picked up
        :param support_multiple: Set to true if multiple utterances of an entity are supported
        :param values: Values extracted by NLU
        :param supported_values: List of supported values for the slot
        :param invalid_trigger: Trigger to use if the extracted value is not supported
        :param key: Dict key to use in the params returned
        :return: a tuple of (filled, partially_filled, trigger, params)    
        """

        trigger = ""
        values = []
        if not body.pick_first and body.support_multiple:
            for value in body.values:
                if value.value not in body.supported_values:
                    trigger = body.invalid_trigger
                else:
                    values.append(value.value.upper())
        elif body.pick_first and not body.support_multiple:
            value = body.values[0]
            if value.value not in body.supported_values:
                    trigger = body.invalid_trigger
            else:
                values = value.value.upper()
                
        else:
            raise HTTPException(status_code=400, detail="pick_first and support_multiple cannot be same")
        partially_filled = bool(values) and bool(trigger)
        filled = bool(values) and not bool(trigger)
        parameters = {body.key: values} if values and not trigger  else {}
        return dict( 
            filled=filled, 
            partially_filled=partially_filled,
            trigger=trigger,
            parameters=parameters)
