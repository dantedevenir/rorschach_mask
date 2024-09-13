mapping_molina_primary_id = {
    "HIX_ID": "member_id",
}

mapping_molina_owner = {
    "Member_First_Name": "first_name",
    "Member_Last_Name": "last_name",
    "dob": "dob",
    "Gender": "gender",
}

mapping_molina_policy = {
    "Broker_NPN": "policy_aor",
    "Effective_date": "effective_date",
    "Paid_Through_Date": "paid_through_date",
    "End_Date": "expiration_date",
    "Member_Premium": "net_premium",
    "Total_Premium": "gross_premium",
    "Status": "policy_status",
    "Member_Count": "household_size",
}

mapping_molina_policy_address = {
    "Address1": "address",
    "City": "city",
    "State": "state",
    "Zip": "zip-code",
}

mapping_molina = {}
mapping_molina.update(mapping_molina_primary_id)
mapping_molina.update(mapping_molina_owner)
mapping_molina.update(mapping_molina_policy)
mapping_molina.update(mapping_molina_policy_address)

