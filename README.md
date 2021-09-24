# WHMCS Exporter
Prometheus exporter for WHMCS installs

## What it provides
WHMCSExporter will output metrics for your Pterodactyl install from the [GetStats](https://developers.whmcs.com/api-reference/getstats/) endpoint.

### Self hosting
Install requests:
`pip install requests`

Modify `PORT` on line 5 to the port you want to use.

Replace `API_URL` with the URL of your WHMCS install following the same format as what is there.

Replace `KEY` with the WHMCS key.

Replace `SECRET` with the WHMCS secret.

I recommend setting up a reverse proxy but it is not necessary.
