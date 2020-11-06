class Config(object):
    # In a production app, store this instead in KeyVault or an environment variable
    # TODO: Enter your client secret from Azure AD below
    CLIENT_SECRET = "BzD.2qT.~7NIdX-fNaO5_D-3c3O1OVLq5N" 

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    # TODO: Enter your application client ID here
    CLIENT_ID = "0a0155a2-9fb7-4ec1-9550-1aeca04250a0"

    # TODO: Enter the redirect path you want to use for OAuth requests
    #   Note that this will be the end of the URI entered back in Azure AD
    REDIRECT_PATH = "/ttnRedirectURIGetToken"  # Used to form an absolute URL, 
        # which must match your app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # So token cache will be stored in server-side session