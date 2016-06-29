'use strict';

// create a student object
// that has a method `addgrade`, that takes a grade from 1 to 5
// an other method `getAverage`, that returns the average of the grades

var Student = {
    grades: [],
    addGrade: function(grade) {
        if (grade < 1 || grade > 5) {
            return 'Invalid value!';
        } else {
            grades.push(grade);
        }
    }
    getAverage: function(grades) {
        
    }
};
