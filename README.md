# tap-process-street

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

This tap:

- Pulls raw data from (http://process.st)
- Outputs the schema for each resource
- Incrementally pulls data based on the input state

---

## Background

Read the Singer Getting Started guide [here](https://github.com/singer-io/getting-started).





## Quick Start

_Install Python3, Pip & Virtual Envs_

1. Install

    ```
    $ pip install tap-process-street
    ```

2. Create the config file

   Create a JSON file called `config.json` based on the `sample-config.json`

   See the Singer docs on config file
   [here](https://github.com/singer-io/getting-started/blob/master/docs/CONFIG_AND_STATE.md#config-file).

4. Run the Tap in Discovery Mode
    ```
    tap-process-street -c config.json -discover > catalog.json
    ```
   
   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode).

5. Update the catalog.json to include the data you want to include in the sync.

   See the Singer docs on stream selection
   [here](https://github.com/singer-io/getting-started/blob/master/docs/SYNC_MODE.md#streamfield-selection) 

5. Run the Tap in Sync Mode
    ```
   tap-chargify -c config.json --catalog catalog-file.json
    ```
   
Copyright &copy; 2020 Process Street
