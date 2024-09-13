mapping_vtigercrm_primary_id = {
    "salesorderid": "salesorder_no",
}

mapping_vtigercrm_id = {
    "cf_2803": "ffm_subscriber_id",
    "cf_2119": "member_id",
}

mapping_vtigercrm_owner = {
    "cf_2293": "first_name",
    "cf_2297": "last_name",
    "cf_2299": "dob",
    "cf_2321": "ssn",
    "cf_2303": "gender",
    "cf_2385": "applying",
}

mapping_vtigercrm_policy = {
    "cf_1513": "last_date_doc",
    "cf_2263": "last_date_change",
    "cf_2069": "issuer",
    "cf_2059": "effective_date",
    "cf_2033": "net_premium",
    "cf_2045": "out_of_pocket_max",
    "cf_2039": "deductible",
    "cf_2067": "policy_aor",
    "cf_1527": "followup_docs",
    "cf_2115": "ffm_app_id",
    "cf_2031": "gross_premium",
    "cf_2035": "plan_hios_id",
    "cf_2193": "expiration_date",
    "cf_2141": "policy_status",
    "cf_2071": "household_size",
    "cf_2025": "household_income",
    "cf_2369": "preferred_language",
    "cf_2261": "paid_through_date",
}

mapping_vtigercrm_policy_auth = { 
    "cf_1489": "user_mp",
    "cf_1491": "password_mp",
}

mapping_vtigercrm_policy_address = {
    "cf_2737": "address",
    "cf_2739": "city",
    "cf_2765": "state",
    "cf_2743": "zip_code",
}

mapping_vtigercrm_spouse = {
    "cf_2347": "spouse_first_name",
    "cf_2351": "spouse_last_name",
    "cf_2357": "spouse_ssn",
    "cf_2359": "spouse_gender",
    "cf_2355": "spouse_dob",
    "cf_2389": "spouse_applying",
}

mapping_vtigercrm_other_1 = {
    "cf_2405": "other_1_first_name",
    "cf_2409": "other_1_last_name",
    "cf_2417": "other_1_ssn",
    "cf_2411": "other_1_gender",
    "cf_2413": "other_1_dob",
    "cf_2401": "other_1_applying",
}

mapping_vtigercrm_other_2 = {
    "cf_2443": "other_2_first_name",
    "cf_2447": "other_2_last_name",
    "cf_2455": "other_2_ssn",
    "cf_2449": "other_2_gender",
    "cf_2451": "other_2_dob",
    "cf_2439": "other_2_applying",
}

mapping_vtigercrm_other_3 = {
    "cf_2479": "other_3_first_name",
    "cf_2483": "other_3_last_name",
    "cf_2491": "other_3_ssn",
    "cf_2485": "other_3_gender",
    "cf_2487": "other_3_dob",
    "cf_2475": "other_3_applying",
}

mapping_vtigercrm_other_4 = {
    "cf_2515": "other_4_first_name",
    "cf_2519": "other_4_last_name",
    "cf_2527": "other_4_ssn",
    "cf_2521": "other_4_gender",
    "cf_2523": "other_4_dob",
    "cf_2511": "other_4_applying",
}

mapping_vtigercrm_other_5 = {
    "cf_2645": "other_5_first_name",
    "cf_2649": "other_5_last_name",
    "cf_2687": "other_5_ssn",
    "cf_2679": "other_5_gender",
    "cf_2681": "other_5_dob",
    "cf_2615": "other_5_applying",
}

mapping_vtigercrm = {}
mapping_vtigercrm.update(mapping_vtigercrm_primary_id)
mapping_vtigercrm.update(mapping_vtigercrm_id)
mapping_vtigercrm.update(mapping_vtigercrm_policy)
mapping_vtigercrm.update(mapping_vtigercrm_policy_auth)
mapping_vtigercrm.update(mapping_vtigercrm_policy_address)
mapping_vtigercrm.update(mapping_vtigercrm_owner)
mapping_vtigercrm.update(mapping_vtigercrm_spouse)
mapping_vtigercrm.update(mapping_vtigercrm_other_1)
mapping_vtigercrm.update(mapping_vtigercrm_other_2)
mapping_vtigercrm.update(mapping_vtigercrm_other_3)
mapping_vtigercrm.update(mapping_vtigercrm_other_4)
mapping_vtigercrm.update(mapping_vtigercrm_other_5)
