import subprocess
import json

def get_openai_api_key_from_op(item_name="OpenAI API Key", field="credential"):
    try:
        # Run the op CLI command to get the item as JSON
        result = subprocess.run(
            ["op", "item", "get", item_name, "--format", "json"],
            check=True,
            capture_output=True,
            text=True
        )
        item_json = json.loads(result.stdout)

        # Search for the field by label
        for field_entry in item_json.get("fields", []):
            if field_entry.get("label") == field:
                return field_entry.get("value")

        raise ValueError(f"Field '{field}' not found in item '{item_name}'.")

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to retrieve item '{item_name}': {e.stderr.strip()}")