from features.json.group_events.file_reader import load_events

def group_events_by_user(obj):
    assist = {}
    for item in obj:
        for key in assist:
            if item['user_id'] == key:
                assist[item['user_id']].append(item)
                break
        else:
            assist[item['user_id']] = [item]

    return list(assist.values())

def main():
    obj = load_events()
    gropedList = group_events_by_user(obj)
    print(gropedList)

if __name__ == "__main__":
    main()