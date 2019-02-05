from temboo.Library.Google.Calendar import GetAllCalendars
from temboo.core.session import TembooSession

# Create a session with your Temboo account details
session = TembooSession("accountName", "myFirstApp", "abc123xxxxxxxxxxxxxx")

# Instantiate the Choreo
getAllCalendarsChoreo = GetAllCalendars(session)

# Get an InputSet object for the Choreo
getAllCalendarsInputs = getAllCalendarsChoreo.new_input_set()

# Set credential to use for execution
getAllCalendarsInputs.set_credential('agnathan')

# Execute the Choreo
getAllCalendarsResults = getAllCalendarsChoreo.execute_with_results(getAllCalendarsInputs)

# Print the Choreo outputs
print("NewAccessToken: " + getAllCalendarsResults.get_NewAccessToken())
print("Response: " + getAllCalendarsResults.get_Response())