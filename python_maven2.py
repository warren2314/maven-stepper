import os

# Get the directory path from the user
directory_path = input("Enter the directory path: ")

# Initialize an empty list for storing artifact and version information
artifact_version_data = []

# Walk through the subdirectories and files
for root, dirs, _ in os.walk(directory_path):
    # Split the relative file path based on the directory separator
    rel_path_parts = os.path.relpath(root, directory_path).split(os.path.sep)

    # Check if the last part of the relative path is a version (assuming it starts with a digit)
    if len(rel_path_parts) > 0 and rel_path_parts[-1][0].isdigit():
        # Concatenate the parts with "." and replace the last "." with "@" before the version
        artifact = ".".join(rel_path_parts[:-1])
        artifact = artifact.rsplit(".", 1)[0] + "/" + artifact.rsplit(".", 1)[1] + "@" + rel_path_parts[-1]

        # Store the artifact and version information
        artifact_version_data.append(f"{artifact}")

# Write the extracted data to a text file
with open("oss_index.txt", "w") as f:
    # Write the header line to the file
    f.write("artifact\n")
    for line in artifact_version_data:
        f.write(line + "\n")

# Print a message to the user
print("The text file has been created.")

