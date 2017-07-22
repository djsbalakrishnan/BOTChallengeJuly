from roombooking.models import Room

def main():
file = open('master_plan.csv', 'r')
for line in file:
	entries = line.split(",")
	obj = Room(room_number=entries[0], type=entries[1], 
		floor=int(entries[2]), lan=bool(entries[3]), phone=bool(entries[4]),
		projector=bool(entries[5]), video_conferencing=bool(entries[6]))
	obj.save()

if __name__ == "__main__":
	main()