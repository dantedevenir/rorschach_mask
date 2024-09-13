from .validate import Validate

validate_primary_id = {
    "ffm_subscriber_id": Validate.to_id_zfill_10,
}

validate_secondary_id = {
    "salesorder_no": Validate.to_id_int,
    "member_id": Validate.to_id_str,
    "ffm_app_id": Validate.to_bigint,
}

validate_policy_basic = {
    "issuer": Validate.to_company,
    "effective_date": Validate.to_datetime,
    "net_premium": Validate.to_float_2,
    "policy_aor": Validate.to_npn,
    "gross_premium": Validate.to_float_2,
    "plan_hios_id": Validate.to_minus,
    "expiration_date": Validate.to_datetime,
    "policy_status": Validate.to_status,
    "paid_through_date": Validate.to_datetime,
}

validate_policy_detail = {
    "last_date_doc": Validate.to_datetime,
    "last_date_change": Validate.to_datetime,  
    "out_of_pocket_max": Validate.to_float_2,
    "deductible": Validate.to_float_deductible,
    "followup_docs": Validate.to_followup_docs,
    "household_size": Validate.to_int_first_1,
    "household_income": Validate.to_float_2,
    "preferred_language": Validate.to_minus,
}

validate_owner = {
    "first_name": Validate.to_minus,
    "last_name": Validate.to_minus,
    "dob": Validate.to_datetime,
    "ssn": Validate.to_int_last_4,
    "gender": Validate.to_minus,
    "applying": Validate.to_boolean,
}

validate_policy_auth = { 
    "user_mp": Validate.to_minus,
    "password_mp": Validate.to_str,
}

validate_address = {
    "address": Validate.to_minus,
    "city": Validate.to_minus,
    "state": Validate.to_minus,
    "zip_code": Validate.to_int_first_5,
}

validate_spouse = {
    "spouse_first_name": Validate.to_minus,
    "spouse_last_name": Validate.to_minus,
    "spouse_ssn": Validate.to_minus,
    "spouse_gender": Validate.to_minus,
    "spouse_dob": Validate.to_datetime,
    "spouse_applying": Validate.to_minus,
}

validate_other_1 = {
    "other_1_first_name": Validate.to_minus,
    "other_1_last_name": Validate.to_minus,
    "other_1_ssn": Validate.to_minus,
    "other_1_gender": Validate.to_minus,
    "other_1_dob": Validate.to_datetime,
    "other_1_applying": Validate.to_minus,
}

validate_other_2 = {
    "other_2_first_name": Validate.to_minus,
    "other_2_last_name": Validate.to_minus,
    "other_2_ssn": Validate.to_minus,
    "other_2_gender": Validate.to_minus,
    "other_2_dob": Validate.to_datetime,
    "other_2_applying": Validate.to_minus,
}

validate_other_3 = {
    "other_3_first_name": Validate.to_minus,
    "other_3_last_name": Validate.to_minus,
    "other_3_ssn": Validate.to_minus,
    "other_3_gender": Validate.to_minus,
    "other_3_dob": Validate.to_datetime,
    "other_3_applying": Validate.to_minus,
}

validate_other_4 = {
    "other_4_first_name": Validate.to_minus,
    "other_4_last_name": Validate.to_minus,
    "other_4_ssn": Validate.to_minus,
    "other_4_gender": Validate.to_minus,
    "other_4_dob": Validate.to_datetime,
    "other_4_applying": Validate.to_minus,
}

validate_other_5 = {
    "other_5_first_name": Validate.to_minus,
    "other_5_last_name": Validate.to_minus,
    "other_5_ssn": Validate.to_minus,
    "other_5_gender": Validate.to_minus,
    "other_5_dob": Validate.to_datetime,
    "other_5_applying": Validate.to_minus,
}

validate = {}
validate.update(validate_primary_id)
validate.update(validate_secondary_id)
validate.update(validate_owner)
validate.update(validate_policy_basic)
validate.update(validate_policy_detail)
validate.update(validate_policy_auth)
validate.update(validate_address)
validate.update(validate_spouse)
validate.update(validate_other_1)
validate.update(validate_other_2)
validate.update(validate_other_3)
validate.update(validate_other_4)
validate.update(validate_other_5)
