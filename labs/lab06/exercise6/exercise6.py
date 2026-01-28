def manage_roster(enrolled, drop_requests, waitlist):
    """
    Processes student drop requests and adds from waitlist if needed.
    
    Args:
        enrolled: Set of currently enrolled student names
        drop_requests: List of student names requesting to drop
        waitlist: Set of students on the waitlist
    
    Returns:
        int: Count of final enrolled students
    """
    
    for student in drop_requests :
            enrolled.discard(student)

    if len(enrolled) < 5:
        wait = list(waitlist)
        for student in wait:
             if len(enrolled) == 7:
                  break
             enrolled.add(student)
          
          
    return len(enrolled)

