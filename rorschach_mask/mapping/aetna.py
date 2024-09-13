mapping_aetna_primary_id = {
    "Issuer Assigned ID": "member_id",
}

mapping_aetna_id = {
    "Exchange Assigned ID": "ffm_subscriber_id"
}

mapping_aetna_owner = {
    "First Name": "first_name",
    "Last Name": "last_name",
    "Date of Birth": "dob",
}

mapping_aetna_policy = {
    "Broker Name": "policy_aor",
    "Paid Through Date": "paid_through_date",
    "Plan ID": "plan_hios_id",
    "Policy Status": "policy_status",
    
}

mapping_aetna = {}
mapping_aetna.update(mapping_aetna_primary_id)
mapping_aetna.update(mapping_aetna_id)
mapping_aetna.update(mapping_aetna_owner)
mapping_aetna.update(mapping_aetna_policy)
