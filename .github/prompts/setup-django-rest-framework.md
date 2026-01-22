Let's setup codespace for the URL, start the server via VS Code launch.json, and test the API.

- All Django project files are in the `octofit-tracker/backend/octofit_tracker` directory.
- Only update urls in `settings.py` and `urls.py`
- REST api endpoint format https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
- example full url: https://$CODESPACE_NAME-8000.app.github.dev/api/activities/
- Do not hard code the `$CODESPACE_NAME` value use the variable
- Do not update the `views.py`

1. Update `urls.py` to replace the return for the REST API URL endpoints with the environment variable $CODESPACE_NAME https://$CODESPACE_NAME-8000.app.github.dev for Django and avoid certificate HTTPS issues.
2. Make sure the Django backend works on your codespace URL and localhost (i.e., the value of `$CODESPACE_NAME`) by updating `ALLOWED_HOSTS` in `settings.py`.
3. Test the API endpoints using curl command.