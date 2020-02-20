class FirestoreRest:
    class Credentials:
            def __init__(self):
                self.expires_at = 0
                self.auth_token = {}
                self.base_path = ""
                self.base_url = ""
                self.refresh()

            def get_access_token(self):
                scope = ['https://www.googleapis.com/auth/cloud-platform','https://www.googleapis.com/auth/datastore']
                serviceAccount = "app_identity.get_service_account_name()"
                token, exp = "scope", "serviceAccount"
                self.auth_token, self.expires_at = token, exp
                
            def setup_db(self, database):
                # email = app_identity.get_service_account_name()
                projectId = "1234"
                self.base_path = "projects/{0}/databases/{1}/".format(projectId, database)
                self.base_url = "https://firestore.googleapis.com/v1/" + self.base_path
            
            def refresh(self, database="(default)"):
                self.get_access_token()
                self.setup_db(database)

    cred = Credentials()
    # def __init__(self):
        # type(self).cred = self.Credentials()
    #     self.cred = self.Credentials()
    #     self.nihao = nihao

    @classmethod
    def makeRequest(cls, url, requestType, body=None, retries=3):
        return body

    @classmethod
    def runQuery(cls, structuredQuery):
        """
            Run the structured query defined according to the Firestore rest API docs, see NetFlowPingApp getItems()
            function as an example
            @param structuredQuery: query the firestore database according to the structure defined by...
            https://firebase.google.com/docs/firestore/reference/rest/v1/StructuredQuery
        """
        # cls(nihao="wobuhao")
        # print(self.nihao)
        url = FirestoreRest.cred.base_url + "documents:runQuery"

        return cls.makeRequest(url, 'POST', structuredQuery)


db = FirestoreRest.runQuery("nihao")
print(db)


