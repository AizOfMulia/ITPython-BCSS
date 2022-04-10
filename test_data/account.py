class account:

    def __init__ (self):
        pass

    # Basic user dictionary to imitate a database or json
    __users : dict    =   {
                            "shazam" :
                            {
                                "password" :

                                # Hash for "Hello"
                                "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969",
                                "name" :
                                "Billy Batson"
                            },

                            "batman" :
                            {
                                "password" :

                                # Hash for "wayne"
                                "a982c97d452cc71fde02409d6e6a623220c882930c3c13ab7733e61bc9870b6c",
                                "name" :
                                "Bruce Wayne"
                            },

                            "hulk" :
                            {
                                "password" :

                                # Hash for Smash
                                "ffb45102177a3d20d4c5d4b2173ed232d7d10ed118ec14766129b1f224a79ba1",
                                "name" :
                                "Bruce Banner"
                            },

                            "spiderman" :
                            {
                                "password" :

                                # Hash for Aunt May
                                "9fd9a72bb51acb8c5d2356f1cefce36eed4eb1e8f93b7a3ad7d6edf74d729f30",
                                "name" :
                                "Peter Parker"
                            },
                        }

    def get_users_list (self):
        return self.__users

    #   Basic getter for user list
    def get_user (self, username):
        return self.__users.get(username)
