class RestConstant(object):
    HTTPGET = "GET"
    HTTPPUT = "PUT"
    HTTPPOST = "POST"
    HTTPDELETE = "DELETE"
    HTTPACCEPT = "Accept"
    CONTENT_LENGTH = "Content-Length"
    CHARSET_UTF8 = "UTF-8"
    BASE_URL = "https://"
    HEADER_APP_KEY = "app_key"
    HEADER_APP_AUTH = "Authorization"

    AUTH_LOGOUT = "/iocm/app/sec/v1.1.0/logout"
    REGISTER_DEVICE_VERIFYCODE_MODE = "/iocm/app/reg/v1.1.0/deviceCredentials"
    REGISTER_DEVICE_SECRET_MODE = "/iocm/app/reg/v2.0.0/deviceCredentials"
    REFRESH_DEVICE_KEY_VERIFICATION_MODE = "/iocm/app/reg/v1.1.0/deviceCredentials/"
    REFRESH_DEVICE_KEY_SECRET_MODE = "/iocm/app/reg/v2.0.0/deviceCredentials/"
    QUERY_DEVICE_ACTIVATION_STATUS = "/iocm/app/reg/v1.1.0/deviceCredentials/"

    APP_AUTH = "/iocm/app/sec/v1.1.0/login"
    REFRESH_TOKEN = "/iocm/app/sec/v1.1.0/refreshToken"

    CREATE_BATCH_TASK = "/iocm/app/batchtask/v1.1.0/tasks/"
    QUERYTASKDETAILS = "/iocm/app/batchtask/v1.1.0/taskDetails?taskId="

    QUERY_SINGLE_DEVICE_INFO = "/iocm/app/dm/v1.4.0/devices/"
    QUERY_BATCH_DEVICES_INFO = "/iocm/app/dm/v1.4.0/devices?"
    QUERY_DEVICE_DATA_HISTORY = "/iocm/app/data/v1.2.0/deviceDataHistory?deviceId="
    QUERY_DEVICE_DESIRED_HISTORY = "/iocm/app/shadow/v1.5.0/deviceDesiredHistory?deviceId="
    QUERY_DEVICE_CAPABILITIES = "/iocm/app/data/v1.1.0/deviceCapabilities?"

    CREATE_DEVICE_GROUP = "/iocm/app/devgroup/v1.3.0/devGroups"
    DELETE_DEVICE_GROUP = "/iocm/app/devgroup/v1.3.0/devGroups/"
    MODIFY_DEVICE_GROUP = "/iocm/app/devgroup/v1.3.0/devGroups/"
    QUERY_DEVICE_GROUPS = "/iocm/app/devgroup/v1.3.0/devGroups?"
    QUERY_SINGLE_DEVICE_GROUP = "/iocm/app/devgroup/v1.3.0/devGroups/"
    QUERY_DEVICE_GROUP_MEMBERS = "/iocm/app/dm/v1.2.0/devices/ids?devGroupId="
    ADD_DEVICES_TO_GROUP = "/iocm/app/dm/v1.1.0/devices/addDevGroupTagToDevices"
    DELETE_DEVICES_FROM_GROUP = "/iocm/app/dm/v1.1.0/devices/deleteDevGroupTagFromDevices"

    REG_DIRECT_DEVICE = "/iocm/app/reg/v1.1.0/deviceCredentials"
    REFRESH_DEVICE_KEY = "/iocm/app/reg/v1.1.0/deviceCredentials/"
    MODIFY_DEVICE_INFO = "/iocm/app/dm/v1.4.0/devices/"
    DELETE_DIRECT_DEVICE = "/iocm/app/dm/v1.4.0/devices/"
    QUERY_DEVICE_STATUS = "/iocm/app/reg/v1.1.0/deviceCredentials/"
    QUERY_DEVICE_REALTIME_LOCATION = "/iocm/app/location/v1.1.0/queryDeviceRealtimeLocation"
    QUERY_DEVICE_SHADOW = "/iocm/app/shadow/v1.5.0/devices/"
    MODIFY_DEVICE_SHADOW = "/iocm/app/shadow/v1.5.0/devices/"

    INVOKE_DEVICE_SERVICE = "/iocm/app/signaltrans/v1.1.0/devices/"

    QUERY_UPGRADE_PACKAGE_LIST = "/iodm/northbound/v1.5.0/category?"
    QUERY_UPGRADE_PACKAGE = "/iodm/northbound/v1.5.0/category/"
    DELETE_UPGRADE_PACKAGE = "/iodm/northbound/v1.5.0/category/"
    CREATE_SOFTWARE_UPGRADE_TASK = "/iodm/northbound/v1.5.0/operations/softwareUpgrade"
    CREATE_FIRMWARE_UPGRADE_TASK = "/iodm/northbound/v1.5.0/operations/firmwareUpgrade"
    QUERY_UPGRADE_TASK = "/iodm/northbound/v1.5.0/operations/"
    QUERY_UPGRADE_SUB_TASK = "/iodm/northbound/v1.5.0/operations/"
    QUERY_UPGRADE_TASK_LIST = "/iodm/northbound/v1.5.0/operations?"

    CREATE_RULE = "/iocm/app/rule/v1.2.0/rules"
    UPDATE_RULE = "/iocm/app/rule/v1.2.0/rules"
    DELETE_RULE = "/iocm/app/rule/v1.2.0/rules/"
    QUERY_RULES = "/iocm/app/rule/v1.2.0/rules?author="
    UPDATE_RULE_STATUS = "/iocm/app/rule/v1.2.0/rules/"
    UPDATE_BATCH_RULE_STATUS = "/iocm/app/rule/v1.2.0/rules/status"

    POST_DEVICE_COMMAND = "/iocm/app/cmd/v1.4.0/deviceCommands"
    QUERY_DEVICE_COMMAND = "/iocm/app/cmd/v1.4.0/deviceCommands?"
    UPDATE_DEVICE_COMMAND = "/iocm/app/cmd/v1.4.0/deviceCommands/"
    CREATE_DEVICE_CMD_CANCEL_TASK = "/iocm/app/cmd/v1.4.0/deviceCommandCancelTasks"
    QUERY_DEVICE_CMD_CANCEL_TASK = "/iocm/app/cmd/v1.4.0/deviceCommandCancelTasks?"

    SUB_DEVICE_BUSINESS_DATA = "/iocm/app/sub/v1.2.0/subscriptions"
    SUB_DEVICE_MANAGEMENT_DATA = "/iodm/app/sub/v1.1.0/subscribe"
    QUERY_SINGLE_SUB_SCRIPTION = "/iocm/app/sub/v1.2.0/subscriptions/"
    QUERY_BATCH_SUB_SCRIPTIONS = "/iocm/app/sub/v1.2.0/subscriptions?"
    DELETE_SINGLE_SUB_SCRIPTION = "/iocm/app/sub/v1.2.0/subscriptions/"
    DELETE_BATCH_SUB_SCRIPTIONS = "/iocm/app/sub/v1.2.0/subscriptions?"
