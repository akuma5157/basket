"""basket API implementation
"""
from datetime import datetime
from .models import SlotValidationnumericRequest, SlotValidationFiniteValuesRequest, SlotValidationResult

class Implementation():
    # get_time -- Synchronisation point for meld
    @staticmethod
    def get_time(*args, **kwargs):
        """
        :param request: An HttpRequest
        """
        return datetime.now().isoformat()

    @staticmethod
    def validate_numeric_entity(body: SlotValidationnumericRequest = None, *args, **kwargs):
        """
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
        :return: a tuple of (filled, partially_filled, trigger, params)    """
        return dict(
            filled=True,
            partially_filled=False,
            trigger="Hello",
            parameters="ChCha")

    @staticmethod
    def validate_finite_values_entity(body: SlotValidationFiniteValuesRequest = None, *args, **kwargs):
        """
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
        return dict(
            filled=True,
            partially_filled=False,
            trigger="Hello",
            parameters="ChCha")
