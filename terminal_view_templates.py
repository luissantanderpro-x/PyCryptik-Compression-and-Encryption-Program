# MARK: - Terminal View Templates 

templates = {
    'main': {
        'header': [
            "Please choose one of the following options\n\n"
        ], 
        'menu_choices': [
            "[X] Compression\n",
            "[ ] Encryption\n",
            "[ ] Decryption\n",
            "[ ] Exit Program\n"
        ],
        'footer': [
            "\npress [ enter ] to proceed with selected option.\n" 
        ]
    }, 
    'compression_main': {
        'header': [
            "Welcome to the compression engine...\nChoose a following compression scheme\n"
        ],
        'menu_choices': [
            "[X] RAR\n",
            "[ ] Return to main menu\n"
        ],
        "footer": [
            "\npress [ enter ] to proceed with selected option.\n" 
        ]
    },
    'compression_yes_or_no_options': {
        'header': [
            "Do you wish to compress the file\n"
        ],
        'menu_choices': [
            '[X] Yes\n',
            '[ ] No\n'
        ],
        'footer': [
            ''
        ]
    },
    'encryption_main': {
        'header': [
            'Welcome to the encryption engine...\nPlease choose one of the following encryption schemes\n\n'
        ],
        'menu_choices': [
            '[X] SHA256\n',
            '[ ] Return to main menu\n'
        ], 
        'footer': [
            '\npress [ enter ] to proceed with selected option.\nNote: Must be compressed with one the following formats\n[.rar]\n'
        ]
    }, 
    'encryption_yes_or_no_options': {
        'header': [
            'Do you wish to encrypt the file?\n\n'
        ],
        'menu_choices': [
            '[X] Yes\n',
            '[ ] No\n'
        ],
        'footer': [
            ''
        ]
    },
    'decryption_main': {
        'header': [
            'Welcome to the decryption engine...\nPlease choose one of the following decryption options\n\n'
        ],
        'menu_choices': [
            '[X] Decrypt a file\n',
            '[ ] Return to main menu\n'
        ],
        'footer': [
            '\npress [ enter ] to proceed with selected option.\n'
        ]
    }
}