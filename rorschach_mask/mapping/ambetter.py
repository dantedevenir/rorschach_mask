mapping_ambetter_primary_id = {
    "Policy Number": "member_id",
}

mapping_ambetter_id = {
    "Exchange Subscriber ID": "ffm_subscriber_id",
}

mapping_ambetter_owner = {
    "Inusred First Name": "first_name",
    "Insured Last Name": "last_name",
    "Member Date Of Birth": "dob",
}

mapping_ambetter_policy = {
    "Broker Name": "policy_aor",
    "Paid Through Date": "paid_through_date",
    "Policy Term Date": "expiration_date",
    "Member Responsibility": "net_premium",
    "Number of Members": "household_size"
}

mapping_ambetter_policy_address = {
    "State": "state",
}

mapping_ambetter = {}
mapping_ambetter.update(mapping_ambetter_primary_id)
mapping_ambetter.update(mapping_ambetter_id)
mapping_ambetter.update(mapping_ambetter_owner)
mapping_ambetter.update(mapping_ambetter_policy)
mapping_ambetter.update(mapping_ambetter_policy_address)