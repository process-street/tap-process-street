# Process Street

## Connecting Process Street

### Requirements

To set up Process Street in Stitch, you need:

- **Access to a Process Street administrator account** This is necessary to login to Process Street and generate an API key.

### Setup

1) Login to Process Street and navigate to the [integrations page](https://app.process.st/organizations/manage/integrations).
2) Generate a new API key or use an existing key. 

---

## Process Street Replication

The Process Street Tap replicates the entire table for every selected stream.  As such it's advisable to tune what data you load to ensure the replication is fast and to keep costs low.

- Optionally specify a start_date to only load a subset of your data.
- Tune your replication frequency to only reload the data when you need it (daily, weekly, monthly). 
- Only select the streams you need, a lot of customers won't need the form field data for example.

---

## Process Street Table Schemas

- Table name: Approvals
- Description: Contains all the task approvals in your organization
- Primary key column(s): id
- Replicated fully or incrementally: fully
- Link to API endpoint documentation: https://developer.process.st/#/paths/~1approvals

- Table name: Checklists
- Description: Contains all the checklists in your organization
- Primary key column(s): id
- Replicated fully or incrementally: fully
- Link to API endpoint documentation: https://developer.process.st/#/paths/~1checklists/get

- Table name: Form Fields
- Description: Contains all the form fields from the templates in your organization
- Primary key column(s): id
- Replicated fully or incrementally: fully
- Link to API endpoint documentation: https://developer.process.st/#/paths/~1form-fields/get

- Table name: Form Field Values
- Description: Contains all the form field values from the checklists in your organization
- Primary key column(s): id
- Replicated fully or incrementally: fully
- Link to API endpoint documentation: https://developer.process.st/#/paths/~1form-field-values/get

- Table name: Tasks
- Description: Contains all the tasks from the checklists in your organization
- Primary key column(s): id
- Replicated fully or incrementally: fully
- Link to API endpoint documentation: https://developer.process.st/#/paths/~1tasks/get

- Table name: Task Templates
- Description: Contains all the task templates from the templates in your organization
- Primary key column(s): id
- Replicated fully or incrementally: fully
- Link to API endpoint documentation: https://developer.process.st/#/paths/~1task-templates/get

- Table name: Users
- Description: Contains all the users in your organization
- Primary key column(s): id
- Replicated fully or incrementally: fully
- Link to API endpoint documentation: https://developer.process.st/#/paths/~1users/get

---

## Troubleshooting / Other Important Info

See the [API Documentation](https://developer.process.st/) for more details about the schemas.
