def FullOTA_PostValidate(info):

  info.script.AppendExtra(
    ('ui_print("Resizing /system...");\n'
    'run_program("/sbin/e2fsck_static", "-fy", "/dev/block/mmcblk0p9");\n'
    'run_program("/sbin/resize2fs_static", "/dev/block/mmcblk0p9");\n'
    'run_program("/sbin/e2fsck_static", "-fy", "/dev/block/mmcblk0p9");'))
