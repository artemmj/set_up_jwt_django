REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'project.exceptions.core_exception_handler',
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'apps.authentication.backends.JWTAuthentication',
    ),
}
