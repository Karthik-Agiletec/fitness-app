def template_constants(request):
    # Define your global constants here
    return {
        'APP_NAME': 'Fitness App',
        'form_elements' : [
                            {"key": "steps", "label": "Steps Per Day"},
                            {"key": "Burned_Calories", "label": "Burned Calories"},
                            {"key": "Distance_in_km", "label": "Distance in KM"},
                            {"key": "active_minutes", "label": "Active Minutes"},
                            {"key": "sleep", "label": "Sleep Hour"},
                            {"key": "heartrate", "label": "Average Heart Rate"},
                           ],
        'packages':[
            {"label":"Normal", "image":"fourth.jpg", "url":"normal" },
            {"label":"Bulk", "image":"second.jpg", "url":"bulk" },
            {"label":"Weight", "image":"pexels-leonardho-1552106.jpg", "url":"weight" }
        ],
        'activity_list':[
            {"label":"Chest", "image":"pexels-anush-1431282.jpg","url":"chest"},
            {"label":"Back", "image":"pexels-muribotelho-1865131.jpg","url":"back"},
            {"label":"Shoulders", "image":"second.jpg","url":"shoulders"},
            {"label":"Upper Arms", "image":"pexels-keiji-yoshiki-31563-176794.jpg","url":"upper_arms"},
            {"label":"Waist", "image":"fourth.jpg","url":"waist"},
        ]
    }

activities = {
    "normal": [
        {"category": "chest", "exercises": [
            {"image": "https://hips.hearstapps.com/hmg-prod/images/workouts/2016/03/archerpushup-1457045156.gif", "title": "Archer push up", "sets": "3 times of set 10"},
            {"image": "https://fitnessprogramer.com/wp-content/uploads/2022/02/Seated-Chest-Stretch.gif", "title": "Assisted seated pectoralis major stretch with stability ball", "sets": "3 times of set 10"},
          
          ]
        },
        {"category": "back", "exercises": [
            {"image": "https://i0.wp.com/post.healthline.com/wp-content/uploads/2022/02/400x400_How_To_Do_The_Lat_Pull_Down_Lat_Pull_Down.gif?h=840", "title": "alternate lateral pulldown", "sets": "3 times of set 10"},
            {"image": "https://www.garagegymreviews.com/wp-content/uploads/archer-pull-up.gif", "title": "archer pull up", "sets": "3 times of set 10"},
          
        ]},
        {"category": "shoulders", "exercises": [
            {"image": "https://gymvisual.com/img/p/4/8/0/7/4807.gif", "title": "barbell rear delt raise", "sets": "3 times of set 10"},
            {"image": "https://i.pinimg.com/originals/82/cc/c7/82ccc7eab6dcb8dba83869cb6c3da713.gif", "title": "band reverse fly", "sets": "3 times of set 10"},
          
        ]},
        {"category": "upper_arms", "exercises": [
            {"image": "https://cdn.jefit.com/assets/img/exercises/gifs/243.gif", "title": "assisted standing triceps extension (with towel)", "sets": "3 times of set 10"},
            {"image": "https://www.sparkpeople.com/assets/exercises/Assisted-Triceps-Dip-Machine.gif", "title": "assisted triceps dip (kneeling)", "sets": "3 times of set 10"},
          
        ]},
        {"category": "waist", "exercises": [
            {"image": "https://img.livestrong.com/-/ppds/1d878326-f44c-469a-979b-7669ee1b57d1.gif", "title": "3/4 sit-up", "sets": "3 times of set 10"},
            {"image": "https://fitnessprogramer.com/wp-content/uploads/2021/05/Bench-Side-Bend.gif", "title": "45Â° side bend", "sets": "3 times of set 10"},
          
        ]},
    ],
    "bulk": [
        {"category": "chest", "exercises": [
            {"image": "https://i.pinimg.com/originals/57/30/31/5730314e8ab933d784e401e6227e296d.gif", "title": "Band bench press", "sets": "3 times of set 10"},
            {"image": "https://fitnessprogramer.com/wp-content/uploads/2022/02/Band-Single-Arm-Shoulder-Press.gif", "title": "Band one arm twisting chest press", "sets": "3 times of set 10"},
          
        ]},
        {"category": "back", "exercises": [
            {"image": "https://www.inspireusafoundation.org/wp-content/uploads/2023/04/close-grip-pull-up.gif", "title": "assisted parallel close grip pull-up", "sets": "3 times of set 10"},
            {"image": "https://gymvisual.com/img/p/1/5/1/6/6/15166.gif", "title": "assisted pull-up", "sets": "3 times of set 10"},
          
        ]},
        {"category": "shoulders", "exercises": [
            {"image": "https://i.pinimg.com/originals/82/cc/c7/82ccc7eab6dcb8dba83869cb6c3da713.gif", "title": "band reverse fly", "sets": "3 times of set 10"},
            {"image": "https://gymvisual.com/img/p/4/7/9/8/4798.gif", "title": "barbell one arm snatch", "sets": "3 times of set 10"},
          
        ]},
        {"category": "upper_arms", "exercises": [
            {"image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3sHmIlmnDgZsjEElRLVAsC87j_3bgT95kQw&s", "title": "band alternating biceps curl", "sets": "3 times of set 10"},
            {"image": "https://gymvisual.com/img/p/2/6/4/5/4/26454.gif", "title": "band close-grip push-up", "sets": "3 times of set 10"},
          
        ]},
        {"category": "waist", "exercises": [
            {"image": "https://homeworkouts.org/wp-content/uploads/anim-air-bike-crunches.gif", "title": "air bike", "sets": "3 times of set 10"},
            {"image": "https://fitnessprogramer.com/wp-content/uploads/2021/02/Hanging-Knee-Raises.gif", "title": "arm slingers hanging bent knee legs", "sets": "3 times of set 10"},
          
        ]},
    ],
    "weight": [
        {"category": "chest", "exercises": [
            {"image": "https://i.pinimg.com/originals/08/60/37/08603700cb6365ab40466f4dd9d49e23.gif", "title": "Barbell bench press", "sets": "3 times of set 10"},
            {"image": "https://i.makeagif.com/media/10-08-2018/_cgaL0.gif", "title": "barbell decline bench press", "sets": "3 times of set 10"},
        ]},
        {"category": "back", "exercises": [
            {"image": "https://media1.tenor.com/m/FdSmFsLOItMAAAAC/back-extension-exercise.gif", "title": "back extension on exercise ball", "sets": "3 times of set 10"},
            {"image": "https://fitnessprogramer.com/wp-content/uploads/2023/06/Back-Lever.gif", "title": "back lever", "sets": "3 times of set 10"},
          
        ]},
        {"category": "shoulders", "exercises": [
            {"image": "https://i.pinimg.com/originals/73/19/1b/73191b4e67d474530f579396ec9c1070.gif", "title": "Barbell front raise", "sets": "3 times of set 10"},
            {"image": "https://gymvisual.com/img/p/5/7/3/0/5730.gif", "title": "band y-raise", "sets": "3 times of set 10"},
          
        ]},
        {"category": "upper_arms", "exercises": [
            {"image": "https://gymvisual.com/img/p/5/6/8/9/5689.gif", "title": "band concentration curl", "sets": "3 times of set 10"},
            {"image": "https://cdn.jefit.com/assets/img/exercises/gifs/116.gif", "title": "barbell alternate biceps curl", "sets": "3 times of set 10"},
          
        ]},
        {"category": "waist", "exercises": [
            {"image": "https://static.voltrx.com/2023/12/1.gif", "title": "arm slingers hanging straight legs", "sets": "3 times of set 10"},
            {"image": "https://img.livestrong.com/-/ppds/1d878326-f44c-469a-979b-7669ee1b57d1.gif", "title": "arms overhead full sit-up (male)", "sets": "3 times of set 10"},
          
        ]},
    ],
}
