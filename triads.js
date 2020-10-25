var notes = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
];

var modifiers = [
    "", "♯", "♭"
];

var qualities = [
    "maj", "min", "dim", "aug"
];

var pickRandom = function(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

var app = new Vue({ 
    el: '#app',
    data: {
        triads: []
    },
    methods: {
        generate: function(event) {
            this.triads = [];
            for (let i = 0; i < 10; i++) {
                this.triads.push({
                    note: pickRandom(notes),
                    modifier: pickRandom(modifiers),
                    quality: pickRandom(qualities)
                });
            }
        }  
    },
});
