/**
 * Basket
 * REST API doc for Basket.
 *
 * OpenAPI spec version: 0.1
 * Contact: akuma5157@gmail.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */
import { SlotValidationNumericRequestValues } from './slotValidationNumericRequestValues';

export interface SlotValidationNumericRequest { 
    invalid_trigger?: string;
    key?: string;
    name?: string;
    reuse?: boolean;
    pick_first?: boolean;
    support_multiple?: boolean;
    type?: Array<string>;
    validation_parser?: string;
    constraint?: string;
    var_name?: string;
    values?: Array<SlotValidationNumericRequestValues>;
}