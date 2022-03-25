class account:

    def __init__ (self):
        pass

    # Basic user dictionary to imitate a database or json
    __users : dict    =   {
                            "shazam" :
                            {
                                "password" :
                                "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969",
                                "name" :
                                "Billy Batson"
                            },

                            "batman" :
                            {
                                "password" :
                                "a982c97d452cc71fde02409d6e6a623220c882930c3c13ab7733e61bc9870b6c",
                                "name" :
                                "Bruce Wayne"
                            },

                            "hulk" :
                            {
                                "password" :
                                "ffb45102177a3d20d4c5d4b2173ed232d7d10ed118ec14766129b1f224a79ba1",
                                "name" :
                                "Bruce Banner"
                            },

                            "spiderman" :
                            {
                                "password" :
                                "9fd9a72bb51acb8c5d2356f1cefce36eed4eb1e8f93b7a3ad7d6edf74d729f30",
                                "name" :
                                "Peter Parker"
                            },
                        }

    #   Basic getter for user list
    def get_users (self):
        return self.__users
