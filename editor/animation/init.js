//Dont change it
requirejs(['ext_editor_io2', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {

        function PigeonsCanvas(options) {
            options = options || {};
            var colorOrange4 = "#F0801A";
            var colorOrange3 = "#FA8F00";
            var colorOrange2 = "#FAA600";
            var colorOrange1 = "#FABA00";

            var colorBlue4 = "#294270";
            var colorBlue3 = "#006CA9";
            var colorBlue2 = "#65A1CF";
            var colorBlue1 = "#8FC7ED";

            var colorGrey4 = "#737370";
            var colorGrey3 = "#9D9E9E";
            var colorGrey2 = "#C5C6C6";
            var colorGrey1 = "#EBEDED";

            var colorWhite = "#FFFFFF";

            var bird = "M14.676,22.594 C14.676,22.594 3.305,21.071 0,10.526 C0,10.526 7.114,13.571 15.517,11.485 C15.517,11.485 16.637,9.906 12.212,5 C12.212,5 25.488,6.128 26.048,13.177 C26.048,13.177 31.763,5.369 38.651,10.639 C40.052,11.711 40.444,13.346 39.436,12.556 C39.436,12.556 34.45,12.556 32.826,18.647 C32.826,18.647 32.266,31.222 15.965,29.53 C15.965,29.53 11.763,33.139 11.763,35 L4.369,32.124 C4.369,32.124 15.293,26.09 14.676,22.594 z";

            var padding = 10;
            var row = 5;
            var cell = 40;

            var attrBird = {"stroke-width": 0, "fill": colorBlue4};
            var attrNumb = {"stroke": colorOrange4, "fill": colorOrange4, "font-size": cell / 2.5, "font-family": "Verdana"};


            var paper;

            this.create = function (dom, feeding) {
                paper = Raphael(dom,
                    Math.min(feeding.length, row) * (cell + padding) - padding,
                    Math.ceil(feeding.length / row) * cell);
                for (var i = 0; i < feeding.length; i++) {
                    var b = paper.set();
                    b.push(paper.path(bird).attr(attrBird));
                    if (feeding[i] !== 0) {
                        b.push(paper.text(cell / 2, cell / 2, feeding[i]).attr(attrNumb));
                    }
                    else {
                        b[0].attr("fill", colorBlue2);
                    }
                    b.transform("t" + ((i % row) * (cell + padding)) + "," +
                        (Math.floor(i / row) * cell));

                }
            }
        }

        var io = new extIO({
            animation: function($expl, data){
                var checkioInput = data.in;
                if (!checkioInput){
                    return;
                }
                var canvas = new PigeonsCanvas();
                canvas.create($expl[0], data.ext["explanation"]);
            },
        });
        io.start();

    }
)
;
