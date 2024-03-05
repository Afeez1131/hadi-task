from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


class CustomUserRateThrottle(UserRateThrottle):
    scope = 'custom_user_rate_limit'
    rate = '50/min'


class CustomAnonRateThrottle(UserRateThrottle):
    scope = 'custom_anon_rate_limit'
    rate = '15/min'
