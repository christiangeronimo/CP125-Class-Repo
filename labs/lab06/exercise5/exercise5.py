def audit_zero_trust(baseline_set, current_log_list):
   current_log_set = set(current_log_list)

   authorized = baseline_set & current_log_set
   alert = current_log_set - baseline_set 
   inactive = baseline_set - current_log_set

   return authorized,alert,inactive 