$('.content')
        .on("dragover", dragOver)
        .on("dragleave", dragOver)
        .on("drop", uploadFiles);
        var IMG;
        var FILE;
        function dragOver(e){
        	e.stopPropagation();
        	e.preventDefault();
        	if (e.type == "dragover") {
        		$(e.target).css({
        			"background-color": "black",
        			"outline-offset": "-20px"
        		});
        	} else {
            	$(e.target).css({
        			"background-color": "gray",
        			"outline-offset": "-10px"
        		});
            }
        }
        function uploadFiles(e) {
            e.stopPropagation();
            e.preventDefault();
            dragOver(e);
        
            e.dataTransfer = e.originalEvent.dataTransfer;
            var files = e.target.files || e.dataTransfer.files;
            if (files.length > 1) {
                alert('한 개씩만 업로드가 가능합니다.');
                return;
            }
            console.log(files[0]);
            if (files[0].type.match(/image.*/)) {
                FILE = files[0];
                IMG = window.URL.createObjectURL(files[0]);
                    $(e.target).css({
                    "background-image": "url(" + IMG + ")",
                    "outline": "none",
                    "background-size": "contain",
                    "background-repeat": "no-repeat",
                    "background-position": "center"
                    //"background-size": "cover"
                    //"background-size": "300px 300px"
                });
            }
            else {
              alert('이미지가 아닙니다.');
              return;
            }
        }
        function uploadServer(){
                //var form = FILE;
                if(FILE){
                    var lang = $("#lang option:selected").val();
                    var opencv = $("#opencv option:selected").val();
                    var formData = new FormData();
                    formData.append("file", FILE);
                    formData.append("lang", lang);
                    formData.append("opencv", opencv);
                    $.ajax({
                        url: '/upload',
                            processData: false,
                            contentType: false,
                            data: formData,
                            type: 'POST',
                            success: function(response){
                                if(response){
                                    $("#ocr-textdata").val(response);
                                }
                            }
                        });
                }
                else {
                    alert('이미지를 먼저 업로드 해주세요.');
                }
    
        }
