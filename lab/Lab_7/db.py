db = {
  "univer_name": "ГУАП",
  "address": "ул.Гастелло, 15",
  "students": [
    {
      "id": 1,
      "name": "Толстой Андрей",
      "age": 19,
      "contacts": {
        "email": "tolstoi@example.com",
        "phone": "+1234567890"
      },
      "group_id": 1
    },
    {
      "id": 2,
      "name": "Краснова Светлана",
      "age": 20,
      "contacts": {
        "email": "krasnova@example.com",
        "phone": "+0987654321"
      },
      "group_id": 1
    },
    {
      "id": 3,
      "name": "Репин Николай",
      "age": 20,
      "contacts": {
        "email": "repin@example.com",
        "phone": "+5678901234"
      },
      "group_id": 2
    },
    {
        "id": 4,
        "name": "Суворова Алина",
        "age": 20,
        "contacts": {
          "email": "suvorova@example.com",
          "phone": "+4878138589"
        },
        "group_id": 2
      }
    
  ],
  "groups": [
    {
      "id": 1,
      "grade": 4326,
      "grup_teacher_id": 1,
      "students_id": [
        1,
        2
      ]
         
    },
    {
      "id": 2,
      "grade": 4322,
      "grup_teacher_id": 2,
      "students_id": [
        3,
        4
      ]
      
    }
  ],
  "teachers": [
    {
      "id": 1,
      "name": "Иванова Елена",
      "courses_id": [
        1
      ],
      "contacts": {
        "email": "ivanova@example.com",
        "phone": "+79817751234"
      }
    },
    {
      "id": 2,
      "name": "Петрова Ирина",
      "courses_id": [
        2
      ],
      "contacts": {
        "email": "petrova@example.com",
        "phone": "+89988776655"
      }
    },
    {
      "id": 3,
      "name": "Силкова Анастасия",
      "courses_id": [
        3
      ],
      "contacts": {
        "email": "silkova@example.com",
        "phone": "+882347695"
      }
    },
    {
      "id": 4,
      "name": "Вилкова Анастасия",
      "courses_id": [
        3
      ],
      "contacts": {
        "email": "vilkova@example.com",
        "phone": "+8082347695"
      }
    }
    
  ],
  "courses": [
    {
      "id": 1,
      "name": "Физика",
      "teachers_id": [
        1
      ]
    },
    {
      "id": 2,
      "name": "История Росии",
      "teachers_id": [
        3
      ]
    },
    {
      "id": 3,
      "name": "Иностранный язык",
      "teachers_id": [
        2
      ]
    }
  ]
}