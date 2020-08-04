#!
"""

example loading and modularising ppmac code

"""

from os import path
from pmac_config_manager import pmac_modulars as pm

stager = pm.stager(verbose_level=2)

src_full_path = path.abspath(
    r"C:\Users\afsharn\gitdir\psych\outdir\NA_brake_test\Configuration\pp_save.cfg"
)

src_path, src_filename = path.split(path.abspath(src_full_path))

stager.stage(
    f"Loading ppmac native code from file {src_full_path}", this_verbose_level=1
)


with open(src_full_path, "r") as f:
    ppmac_script = f.read()
    f.close()

stager.stage(f"Modularising ppmac code...", this_verbose_level=1)

for i in [1, 2, 3, 4, 5, 6, 7, 8]:

    axis_settings_dict = pm.ppmacExtractModules(
        code_source=ppmac_script, include_tailing=True, motor_index=i, deindex=True,
    )

    axis_config_script = "\n".join(
        f"{key}={axis_settings_dict[key]}" for key in axis_settings_dict
    )

    out_full_name = path.join(src_path, f"{src_filename.rsplit('.')[0]}.motor_{i}.cfg")

    stager.stage(
        f"\nmotor_{i} config saving.------------ \n\n",
        this_verbose_level=2,
        laps_time=True,
    )

    with open(out_full_name, "w+") as f:
        f.write(axis_config_script)
        f.close()


stager.stage(f"Done.", this_verbose_level=0)

print(f"\n\ntime lapses in seconds: {stager.time_laps}")

print("program terminated.")

exit(0)
