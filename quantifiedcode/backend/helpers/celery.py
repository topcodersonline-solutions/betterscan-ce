"""
This file is part of Betterscan CE (Community Edition).

Betterscan is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Betterscan is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with Betterscan. If not, see <https://www.gnu.org/licenses/>.

Originally licensed under the BSD-3-Clause license with parts changed under
LGPL v2.1 with Commons Clause.
See the original LICENSE file for details.

"""

#we use this to map Celery 3 config names to Celery 4 config names
config_mapping_3_4 = {
    'accept_content' : 'CELERY_ACCEPT_CONTENT',
    'enable_utc' : 'CELERY_ENABLE_UTC',
    'imports' : 'CELERY_IMPORTS',
    'include' : 'CELERY_INCLUDE',
    'timezone' : 'CELERY_TIMEZONE',
    'beat_max_loop_interval' : 'CELERYBEAT_MAX_LOOP_INTERVAL',
    'beat_schedule' : 'CELERYBEAT_SCHEDULE',
    'beat_scheduler' : 'CELERYBEAT_SCHEDULER',
    'beat_schedule_filename' : 'CELERYBEAT_SCHEDULE_FILENAME',
    'beat_sync_every' : 'CELERYBEAT_SYNC_EVERY',
    'broker_url' : 'BROKER_URL',
    'broker_transport' : 'BROKER_TRANSPORT',
    'broker_transport_options' : 'BROKER_TRANSPORT_OPTIONS',
    'broker_connection_timeout' : 'BROKER_CONNECTION_TIMEOUT',
    'broker_connection_retry' : 'BROKER_CONNECTION_RETRY',
    'broker_connection_max_retries' : 'BROKER_CONNECTION_MAX_RETRIES',
    'broker_failover_strategy' : 'BROKER_FAILOVER_STRATEGY',
    'broker_heartbeat' : 'BROKER_HEARTBEAT',
    'broker_login_method' : 'BROKER_LOGIN_METHOD',
    'broker_pool_limit' : 'BROKER_POOL_LIMIT',
    'broker_use_ssl' : 'BROKER_USE_SSL',
    'cache_backend' : 'CELERY_CACHE_BACKEND',
    'cache_backend_options' : 'CELERY_CACHE_BACKEND_OPTIONS',
    'cassandra_table' : 'CASSANDRA_COLUMN_FAMILY',
    'cassandra_entry_ttl' : 'CASSANDRA_ENTRY_TTL',
    'cassandra_keyspace' : 'CASSANDRA_KEYSPACE',
    'cassandra_port' : 'CASSANDRA_PORT',
    'cassandra_read_consistency' : 'CASSANDRA_READ_CONSISTENCY',
    'cassandra_servers' : 'CASSANDRA_SERVERS',
    'cassandra_write_consistency' : 'CASSANDRA_WRITE_CONSISTENCY',
    'couchbase_backend_settings' : 'CELERY_COUCHBASE_BACKEND_SETTINGS',
    'mongodb_backend_settings' : 'CELERY_MONGODB_BACKEND_SETTINGS',
    'event_queue_expires' : 'CELERY_EVENT_QUEUE_EXPIRES',
    'event_queue_ttl' : 'CELERY_EVENT_QUEUE_TTL',
    'event_queue_prefix' : 'CELERY_EVENT_QUEUE_PREFIX',
    'event_serializer' : 'CELERY_EVENT_SERIALIZER',
    'redis_db' : 'CELERY_REDIS_DB',
    'redis_host' : 'CELERY_REDIS_HOST',
    'redis_max_connections' : 'CELERY_REDIS_MAX_CONNECTIONS',
    'redis_password' : 'CELERY_REDIS_PASSWORD',
    'redis_port' : 'CELERY_REDIS_PORT',
    'result_backend' : 'CELERY_RESULT_BACKEND',
    'result_cache_max' : 'CELERY_MAX_CACHED_RESULTS',
    'result_compression' : 'CELERY_MESSAGE_COMPRESSION',
    'result_exchange' : 'CELERY_RESULT_EXCHANGE',
    'result_exchange_type' : 'CELERY_RESULT_EXCHANGE_TYPE',
    'result_expires' : 'CELERY_TASK_RESULT_EXPIRES',
    'result_persistent' : 'CELERY_RESULT_PERSISTENT',
    'result_serializer' : 'CELERY_RESULT_SERIALIZER',
    'Use' : 'result_backend instead. CELERY_RESULT_DBURI',
    'database_engine_options' : 'CELERY_RESULT_ENGINE_OPTIONS',
    'database_short_lived_sessions' : '[...]_DB_SHORT_LIVED_SESSIONS',
    'database_db_names' : 'CELERY_RESULT_DB_TABLE_NAMES',
    'security_certificate' : 'CELERY_SECURITY_CERTIFICATE',
    'security_cert_store' : 'CELERY_SECURITY_CERT_STORE',
    'security_key' : 'CELERY_SECURITY_KEY',
    'task_acks_late' : 'CELERY_ACKS_LATE',
    'task_always_eager' : 'CELERY_ALWAYS_EAGER',
    'task_annotations' : 'CELERY_ANNOTATIONS',
    'task_compression' : 'CELERY_MESSAGE_COMPRESSION',
    'task_create_missing_queues' : 'CELERY_CREATE_MISSING_QUEUES',
    'task_default_delivery_mode' : 'CELERY_DEFAULT_DELIVERY_MODE',
    'task_default_exchange' : 'CELERY_DEFAULT_EXCHANGE',
    'task_default_exchange_type' : 'CELERY_DEFAULT_EXCHANGE_TYPE',
    'task_default_queue' : 'CELERY_DEFAULT_QUEUE',
    'task_default_rate_limit' : 'CELERY_DEFAULT_RATE_LIMIT',
    'task_default_routing_key' : 'CELERY_DEFAULT_ROUTING_KEY',
    'task_eager_propagates' : 'CELERY_EAGER_PROPAGATES_EXCEPTIONS',
    'task_ignore_result' : 'CELERY_IGNORE_RESULT',
    'task_publish_retry' : 'CELERY_TASK_PUBLISH_RETRY',
    'task_publish_retry_policy' : 'CELERY_TASK_PUBLISH_RETRY_POLICY',
    'task_queues' : 'CELERY_QUEUES',
    'task_routes' : 'CELERY_ROUTES',
    'task_send_sent_event' : 'CELERY_SEND_TASK_SENT_EVENT',
    'task_serializer' : 'CELERY_TASK_SERIALIZER',
    'task_soft_time_limit' : 'CELERYD_TASK_SOFT_TIME_LIMIT',
    'task_time_limit' : 'CELERYD_TASK_TIME_LIMIT',
    'task_track_started' : 'CELERY_TRACK_STARTED',
    'worker_agent' : 'CELERYD_AGENT',
    'worker_autoscaler' : 'CELERYD_AUTOSCALER',
    'worker_concurrency' : 'CELERYD_CONCURRENCY',
    'worker_consumer' : 'CELERYD_CONSUMER',
    'worker_direct' : 'CELERY_WORKER_DIRECT',
    'worker_disable_rate_limits' : 'CELERY_DISABLE_RATE_LIMITS',
    'worker_enable_remote_control' : 'CELERY_ENABLE_REMOTE_CONTROL',
    'worker_hijack_root_logger' : 'CELERYD_HIJACK_ROOT_LOGGER',
    'worker_log_color' : 'CELERYD_LOG_COLOR',
    'worker_log_format' : 'CELERYD_LOG_FORMAT',
    'worker_lost_wait' : 'CELERYD_WORKER_LOST_WAIT',
    'worker_max_tasks_per_child' : 'CELERYD_MAX_TASKS_PER_CHILD',
    'worker_pool' : 'CELERYD_POOL',
    'worker_pool_putlocks' : 'CELERYD_POOL_PUTLOCKS',
    'worker_pool_restarts' : 'CELERYD_POOL_RESTARTS',
    'worker_prefetch_multiplier' : 'CELERYD_PREFETCH_MULTIPLIER',
    'worker_redirect_stdouts' : 'CELERYD_REDIRECT_STDOUTS',
    'worker_redirect_stdouts_level' : 'CELERYD_REDIRECT_STDOUTS_LEVEL',
    'worker_send_task_events' : 'CELERYD_SEND_EVENTS',
    'worker_state_db' : 'CELERYD_STATE_DB',
    'worker_task_log_format' : 'CELERYD_TASK_LOG_FORMAT',
    'worker_timer' : 'CELERYD_TIMER',
    'worker_timer_precision' : 'CELERYD_TIMER_PRECISION'
}
