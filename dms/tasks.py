
from django.utils import timezone

from .models import Department
from datetime import datetime
import datetime
from django.utils import timezone
from datetime import date
today = date.today()
d2  = today.strftime("%Y")



def test_job():
    """
    Deletes all Departments that are inactive
    """
    #one_minute_ago = timezone.now() - timezone.timedelta(minutes=1)
    # expired_discounts = Discount.objects.filter(created_at__lte=one_minute_ago)
    # expired_discounts.delete()
    
    depart = Department.objects.filter(status='active')
    for list in depart:
        set_inactive1 = today - list.entry_date 
        set_inactive = (abs((set_inactive1).days))
        set_inactive = (int(set_inactive))
        retention_count = ( int(list.retention_count))
        if list.retention == 'Inactive':
            if set_inactive > retention_count:
                set_item_inactive = Department.objects.filter(id=list.id).update(status='inactive', update_date=today)
                print('i am working')
        
    
