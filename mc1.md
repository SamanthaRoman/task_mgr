# Mini Challenge 1

## Create tooling for update and delete

### Acceptance Criteria

1. Create a script to update an existing task.
   1.1. The script should prompt the user for a task id
   1.2. The script should display the existing task (unmodified)
   1.3. The scipt should allow the user to define values for summary, description and is_done
   1.4. The script should allow the user to update the target task (via it's ID)
2. Create a script to delete an existing task
   2.1. The script should prompt the user for a task id
   2.2. The script should allow the user to confirm (or decline) deletion
   2.2. If the user confirms, the script should delete the target task

### Notes

```
Example of GET request using python requests:
response = requests.get(URL)

Example of PUT request using python requests:
response = requests.put(URL, json=something)

Example of DELETE request using python requests:
response = requests.delete(URL)
```
