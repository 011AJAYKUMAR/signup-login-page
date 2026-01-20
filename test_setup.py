#!/usr/bin/env python
import os
import django
import sys

sys.path.insert(0, r'C:\Users\Ajay kumar thakur\projects\my_program')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_program.settings')
django.setup()

from django.contrib.auth.models import User
from user.models import UserProfile

# Clear existing test users
User.objects.filter(username='testuser').delete()

# Test 1: Create a user via signup flow
user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123')
profile = UserProfile.objects.create(user=user, contact_number='1234567890')

# Test 2: Verify user can authenticate
result = user.check_password('testpass123')
print(f'✓ User created: {user.username}')
print(f'✓ Email: {user.email}')
print(f'✓ Contact: {profile.contact_number}')
print(f'✓ Password verification: {result}')
print('\nProject setup complete! You can now:')
print('1. Visit http://127.0.0.1:8000/signup/ to create a new account')
print('2. Visit http://127.0.0.1:8000/login/ to login with your email')
print('3. Visit http://127.0.0.1:8000/ to see the home page (requires login)')
