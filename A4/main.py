# Behnam Baharmand
# A4: Image Manipulation with Python
# Version 0.1.0

# Import resources
import time
import goodies
import functions as fn

start_time = time.time()  # Let's see how long it takes to run the code

### 0. Init ==============================================================
goodies.echo_badge()  # For aesthetic purposes only @-}

### 1. import the images and generate a list in ascending order list. ====
selected_channel = "r"

print(f"▐░ RGB Analysis now underway...")
print(
    f"▐░ Here is the desired list for channel {selected_channel.upper()}و in ascending order:\n"
)

print("\n".join([str(v) for v in fn.calc_mean(fn.images_list, selected_channel)]))

### 2. Generate Collage. =================================================
goodies.insert_new_segment()

fn.nonuple_collage_builder()  # Let's call our nonuple-c generator
print(f"▐░░ Your nonuple college is now created. (collage.png)")

print("▐░░░ Processs finished in: %s seconds\n" % round((time.time() - start_time), 3))
