from datetime import datetime
import pytz

timeZone = pytz.timezone(input('Enter Timezone: '))
local = datetime.now(timeZone)

print(timeZone, local.strftime('%I:%M %p'))