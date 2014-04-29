# Django LDAP authentication

This application uses [django-auth-ldap][] to authenticate against DDH's LDAP
service. If the LDAP authentication fails it falls back to Django
authentication, so it is possible to have local Django accounts.

## Configuration

- Add ddhldap_django to your project
- Install the [requirements][]
- Add the setting `LDAP_GROUP` to your project and set it to the LDAP group you
  want to authenticate to, for example `LDAP_GROUP = 'histpag'`.
- Import the ddhldap_django settings into your project. These settings need to
  be imported after any other settings you might already be importing: `from ddhldap_django.settings import *`.
- Add ddhldap_django signal handler into your project urls:
    
        from ddhldap.signal_handlers import register_signal_handlers as \
            ddhldap_register_signal_hadlers
        ddhldap_register_signal_handlers()

## System requirements

The python/django LDAP libraries depend on the libldap-dev and libsasl-dev system
libraries.

[django-auth-ldap]: http://pythonhosted.org/django-auth-ldap/
[requirements]: requirements.txt
