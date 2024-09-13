mapping_healthsherpa_primary_id = {
    "ffm_subscriber_id": "ffm_subscriber_id",
}
mapping_healthsherpa_id = {
    "salesorder_no": "salesorder_no",
    "member_id": "member_id",
}
mapping_healthsherpa_owner = {
    "first_name": "first_name",
    "last_name": "last_name",
    "ssn": "ssn",
    "gender": "gender",
    "dob": "dob",
    "applying": "applying",
}

mapping_healthsherpa_spouse = {
    "spouse_first_name": "spouse_first_name",
    "spouse_last_name": "spouse_last_name",
    "spouse_ssn": "spouse_ssn",
    "spouse_gender": "spouse_gender",
    "spouse_dob": "spouse_dob",
    "spouse_applying": "spouse_applying",
}

mapping_healthsherpa_other_1 = {
    "other_1_first_name": "other_1_first_name",
    "other_1_last_name": "other_1_last_name",
    "other_1_ssn": "other_1_ssn",
    "other_1_gender": "other_1_gender",
    "other_1_dob": "other_1_dob",
    "other_1_applying": "other_1_applying",
}

mapping_healthsherpa_other_2 = {
    "other_2_first_name": "other_2_first_name",
    "other_2_last_name": "other_2_last_name",
    "other_2_ssn": "other_2_ssn",
    "other_2_gender": "other_2_gender",
    "other_2_dob": "other_2_dob",
    "other_2_applying": "other_2_applying",
}

mapping_healthsherpa_other_3 = {
    "other_3_first_name": "other_3_first_name",
    "other_3_last_name": "other_3_last_name",
    "other_3_ssn": "other_3_ssn",
    "other_3_gender": "other_3_gender",
    "other_3_dob": "other_3_dob",
    "other_3_applying": "other_3_applying",
}

mapping_healthsherpa_other_4 = {
    "other_4_first_name": "other_4_first_name",
    "other_4_last_name": "other_4_last_name",
    "other_4_ssn": "other_4_ssn",
    "other_4_gender": "other_4_gender",
    "other_4_dob": "other_4_dob",
    "other_4_applying": "other_4_applying",
}

mapping_healthsherpa_other_5 = {
    "other_5_first_name": "other_5_first_name",
    "other_5_last_name": "other_5_last_name",
    "other_5_ssn": "other_5_ssn",
    "other_5_gender": "other_5_gender",
    "other_5_dob": "other_5_dob",
    "other_5_applying": "other_5_applying",
}

mapping_healthsherpa_policy = {
    "date_effectuated": "last_date_change",
    "issuer": "issuer",
    "effective_date": "effective_date",
    "net_premium": "net_premium",
    "out_of_pocket_max": "out_of_pocket_max",
    "deductible": "deductible",
    "policy_aor": "policy_aor",
    "followup_docs": "followup_docs",
    "ffm_app_id": "ffm_app_id",
    "gross_premium": "gross_premium",
    "plan_hios_id": "plan_hios_id",
    "expiration_date": "expiration_date",
    "policy_status": "policy_status",
    "household_size": "household_size",
    "household_income": "household_income",
    "preferred_language": "preferred_language",
    "paid_through_date": "paid_through_date",
}

mapping_healthsherpa_policy_address = {
    "address": "address",
    "city": "city",
    "state": "state",
    "zip_code": "zip_code",
}

mapping_healthsherpa = {}
mapping_healthsherpa.update(mapping_healthsherpa_primary_id)
mapping_healthsherpa.update(mapping_healthsherpa_id)
mapping_healthsherpa.update(mapping_healthsherpa_policy)
mapping_healthsherpa.update(mapping_healthsherpa_policy_address)
mapping_healthsherpa.update(mapping_healthsherpa_owner)
mapping_healthsherpa.update(mapping_healthsherpa_spouse)
mapping_healthsherpa.update(mapping_healthsherpa_other_1)
mapping_healthsherpa.update(mapping_healthsherpa_other_2)
mapping_healthsherpa.update(mapping_healthsherpa_other_3)
mapping_healthsherpa.update(mapping_healthsherpa_other_4)
mapping_healthsherpa.update(mapping_healthsherpa_other_5)
