function update_video(video_index_advance, video_index=0){
    console.log(video_index_advance);

    if (video_index_advance != 0){    
        video_index = current_video + video_index_advance;
        if (video_index < 0) video_index = 0;
        if (video_index >=  video_list_size) video_index = video_list_size -1;
    }

    var video = result_list[video_index];
    videoId = video.id.videoId;

    $("iframe#show_video").attr('src', 'https://www.youtube.com/embed/'+videoId)
    current_video = video_index;            
    $("span#current_video").html(current_video+1);
}

function build_video_list(){

    $(result_list).each(function(index, element){
        
        var line = "<tr>";
        line += "<td>"+(index+1)+"</td>";
        line += "<td>";
        line += "<a style='cursor:pointer;' data-dismiss='modal' onClick='update_video(0, "+index+");'>";
        line += "<img width=100 src='"+element.snippet.thumbnails.medium.url+"' /></td>";
        line += "<td>"+element.snippet.channelTitle+"</td>";
        line += "<td> <a style='color:blue; cursor:pointer;' data-dismiss='modal' onClick='update_video(0, "+index+");'>"+element.snippet.title+"</a></td>";
        line += "<td>"+element.snippet.publishedAt+"</td></tr>";

        $("tbody#body_video_list").append(line);
        
    });

}
