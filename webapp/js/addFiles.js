$(window).load(function(){
    $('#drop').click(function(){
        console.log('click');
        $('#fileBox').trigger('click');
    });
    //Remove item
    $('.fileCont span').click(function(){
        $(this).remove();
    });
});
if (window.FileReader) {
    var drop;
    addEventHandler(window, 'load', function () {
        var status = document.getElementById('status');
        drop = document.getElementById('drop');
        var list = document.getElementById('list');

        function cancel(e) {
            if (e.preventDefault) {
                e.preventDefault();
            }
            return false;
        }

        // Tells the browser that we *can* drop on this target
        addEventHandler(drop, 'dragover', cancel);
        addEventHandler(drop, 'dragenter', cancel);

        addEventHandler(drop, 'drop', function (e) {
            e = e || window.event; // get window.event if e argument missing (in IE)   
            if (e.preventDefault) {
                e.preventDefault();
            } // stops the browser from redirecting off to the image.

            var dt = e.dataTransfer;
            var files = dt.files;
            for (var i = 0; i < files.length; i++) {
                var file = files[i];
                var reader = new FileReader();

                //attach event handlers here...

                reader.readAsDataURL(file);
                addEventHandler(reader, 'loadend', function (e, file) {
                    var bin = this.result;
                    var fileCont = document.createElement('div');
                    fileCont.className = "fileCont";
                    list.appendChild(fileCont);
                                        
                    var fileNumber = list.getElementsByTagName('img').length + 1;
                    status.innerHTML = fileNumber < files.length ? 'Loaded 100% of file ' + fileNumber + ' of ' + files.length + '...' : 'Done loading. processed ' + fileNumber + ' files.';

                    var newFile = document.createElement('div');
                    newFile.innerHTML = file.name;
                    newFile.className = "fileName";
                    fileCont.appendChild(newFile);
                    
                    var fileSize = document.createElement('div');
                    fileSize.className = "fileSize";
                    fileSize.innerHTML = Math.round(file.size/1024) + ' KB';
                    fileCont.appendChild(fileSize);
                    
                    var progress = document.createElement('div');
                    progress.className = "progress";
                    progress.innerHTML = '<div aria-valuemax="100" aria-valuemin="0" aria-valuenow="100" class="progress-bar progress-bar-success" role="progressbar" style="width: 100%"></div>';
                    fileCont.appendChild(progress);
                    
                    var remove = document.createElement('div');
                    remove.className = "remove";
                    remove.innerHTML = '<span class="glyphicon glyphicon-remove"></div>';
                    list.appendChild(remove);
                    
                }.bindToEventHandler(file));
            }
            return false;
        });
        Function.prototype.bindToEventHandler = function bindToEventHandler() {
            var handler = this;
            var boundParameters = Array.prototype.slice.call(arguments);
            //create closure
            return function (e) {
                e = e || window.event; // get window.event if e argument missing (in IE)   
                boundParameters.unshift(e);
                handler.apply(this, boundParameters);
            }
        };
    });
} else {
    document.getElementById('status').innerHTML = 'Your browser does not support the HTML5 FileReader.';
}


function addEventHandler(obj, evt, handler) {
    if (obj.addEventListener) {
        // W3C method
        obj.addEventListener(evt, handler, false);
    } else if (obj.attachEvent) {
        // IE method.
        obj.attachEvent('on' + evt, handler);
    } else {
        // Old school method.
        obj['on' + evt] = handler;
    }
}


//Not plugged yet
var bar = $('.progress-bar');
$(function(){
  $(bar).each(function(){
    bar_width = $(this).attr('aria-valuenow');
    $(this).width(bar_width + '%');
  });
});