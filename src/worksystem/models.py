from django.db import models


class WorkInformation(models.Model):
    work_title = models.CharField(max_length=50)
    work_value = models.FloatField()
    time_estimation = models.BigIntegerField()
    employer = models.CharField(max_length=50)
    description = models.CharField(max_length=300, blank=True, null=True)

    def logical_time_estimation(self):
        time = int(self.time_estimation)
        return "{}w {}d {}h {}m {}s".format(time // (7 * 24 * 60 * 60),
                                            (time % (7 * 24 * 60 * 60)) // (24 * 60 * 60),
                                            (time % (24 * 60 * 60)) // (60 * 60),
                                            (time % (60 * 60)) // 60, (time % 60))
