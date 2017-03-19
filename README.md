# Strava-Auto-Uploader
An automatic Strava uploader for Garmin watches.

Designed to run on a Raspberry Pi.

This will automatically upload all activity, since the last sync, to the specified Strava account every time you connect your device.



## Installation

1. Setup your Raspberry Pi or other computer (tested on Raspbian Jesse).
2. Copy `10_garmin_upload` to `/etc/usbmount/mount.d/10_garmin_upload`
3. Give execute permissions to `10_garmin_upload` (`sudo chmod +x /etc/usbmount/mount.d/10_garmin_upload`).
4. Modify `garmin_upload.py` and replace `INSERT_ACCESS_TOKEN_HERE` with your Strava access token.
5. (Optional) Touch `garmin_last_run` with the date you want to start syncing from. `touch -t 201703192127 garmin_last_run`
6. Plug in your watch. Observe Strava syncing.

## Questions, Help, etc
Email chris@ceejaycee.net.


