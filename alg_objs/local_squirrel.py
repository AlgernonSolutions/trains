import os


class SecretSquirrel:
    @classmethod
    def retrieve_credentials(cls, secondary=False, folder_name='algernon_challenge', file_name='keys.txt', **kwargs):
        home_path = os.path.expanduser('~')
        key_file_path = os.path.join(home_path, folder_name, file_name)
        with open(key_file_path, 'r') as key_file:
            key_value = key_file.readline()
            if secondary is True:
                key_value = key_file.readline()
            key_value = key_value.rstrip()
            return key_value
