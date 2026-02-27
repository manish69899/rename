# User ka data yahan rahega (RAM me)
# Structure: { user_id: { 'files': [], 'mode': None, 'step': 'idle' } }

user_data = {}

def get_data(user_id):
    if user_id not in user_data:
        user_data[user_id] = {'files': [], 'mode': None, 'step': 'idle'}
    return user_data[user_id]

def clear_data(user_id):
    if user_id in user_data:
        del user_data[user_id]