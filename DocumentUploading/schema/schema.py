from cerberus import Validator

schema = {
    "adhar_details": {
        "type": "dict",
        "required": True,
        "schema": {
            'name': {'type': 'string', 'required': True},
            'identity_card_no': {'type': 'string', 'required': True},
            'date_of_birth': {'type': 'string', 'regex': r'^\d{4}-\d{2}-\d{2}$', 'required': True},
            'sex': {'type': 'string', 'allowed': ['M', 'F'], 'required': True},
            'address': {'type': 'string', 'required': True},
            'country': {'type': 'string', 'required': True}
        }
    },
    "dl_details": {
        "type": "dict",
        "required": True,
        "schema": {
            'name': {'type': 'string', 'required': True},
            'identity_card_no': {'type': 'string', 'required': True},
            'date_of_birth': {'type': 'string', 'regex': r'^\d{4}-\d{2}-\d{2}$', 'required': True},
            'sex': {'type': 'string', 'allowed': ['M', 'F'], 'required': True},
            'address': {'type': 'string', 'required': True},
            'country': {'type': 'string', 'required': True}
        }
    },
    "info_match_score": {'type': 'integer', 'min': 1, 'max': 10, 'required': True},
    "customer_valid": {'type': 'boolean', 'required': True},
    "kyc_status": {
        'type': 'string',
        'allowed': ['verified', 'not_verified'],
        'required': True,
        'default': 'not_verified'  # default goes *inside* the field dict
    }
}

validator = Validator(schema, purge_unknown=True)
