#------------------------------------------------------------------------------
# http://pythonhosted.org/django-auth-ldap/
#------------------------------------------------------------------------------

from django.conf import settings as s
from django_auth_ldap.config import LDAPSearch, PosixGroupType

import ldap

LDAP_GROUP = 'cn=' + s.LDAP_GROUP
LDAP_BASE_DC = 'dc=dighum,dc=kcl,dc=ac,dc=uk'
LDAP_BASE_OU = 'ou=groups,' + LDAP_BASE_DC

# Baseline configuration
AUTH_LDAP_SERVER_URI = 'ldap://ldap1.cch.kcl.ac.uk'
AUTH_LDAP_BIND_DN = ''
AUTH_LDAP_BIND_PASSWORD = ''
AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,ou=people,' + LDAP_BASE_DC

# Set up the basic group parameters
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    LDAP_BASE_OU,
    ldap.SCOPE_SUBTREE,
    '(objectClass=posixGroup)'
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr='cn')

# Simple group restrictions
AUTH_LDAP_REQUIRE_GROUP = LDAP_GROUP + ',' + LDAP_BASE_OU

# Populate the Django user from the LDAP directory
AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail'
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    'is_active': 'cn=confluence-users,' + LDAP_BASE_OU,
    'is_staff': 'cn=ddh-staff,' + LDAP_BASE_OU,
    'is_superuser': 'cn=sysadmin,' + LDAP_BASE_OU
}

# This is the default, but I like to be explicit
AUTH_LDAP_ALWAYS_UPDATE_USER = True

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
