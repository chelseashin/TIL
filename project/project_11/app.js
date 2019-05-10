const app = new Vue({
  el: "#app",
  data: {
    logo: 'MO<i class="fab fa-vuejs"></i>IE',
    isMain: true,
    genres: [],
    movies: [ // 현재 하드 타이핑 된 배열이지만, 실제로는 axios.get() 을 통해 API server 로 부터 받아옵니다.
    ],
    detailView: false, // 현재 방식의 목록/상세 화면 전환에 사용되는 flag 입니다.
    movieDetail: {
        newScore : 0,
        newComment : '',
    },  // 상세 화면에서 출력할 때 사용할 영화 객체입니다.
  },
  methods: {
    toggleDetail: function(id=null) {  // 목록 <=> 상세 화면을 전환합니다. 인자로 id 가 들어올 경우, 상세화면을 표시합니다.
      if (id) {
        const movie = this.movies[id-1]  // 현재는 무조건 $data.movies 의 첫 번째 영화를 선택합니다. 실제로는 인자로 넘어온 id 를 통해 특정 영화를 찾습니다.

        // Better way..?
        this.movieDetail.id = id
        this.movieDetail.title = movie.title
        this.movieDetail.audience= movie.audience
        this.movieDetail.poster_url= movie.poster_url
        this.movieDetail.description = movie.description
        this.movieDetail.scores = movie.score_set  // 상세 페이지에서 표시할 모든 $data.scores 를 받아와야 합니다.
        this.movieDetail.genre = this.genres[movie.genre-1].name // 해당 movie 의 genreId 를 통해 genre.name 을 찾아서 저장합니다.
    }
      this.detailView = !this.detailView
    },
    // 추가
    getMovies: function () {
      axios.get('http://django-intro-chelseashin.c9users.io:8080/api/v1/movies/')
            .then(response => response.data)
            .then(movies => {
              this.movies = movies.map(movie => {
                  let sum = 0
                  for (let i = 0; i < movie.score_set.length; i++){
                      sum += movie.score_set[i].score
                  }
                  let rescore = sum/movie.score_set.length
                  return {...movie, score: rescore.toFixed(2)}
                })
            })
            .catch(error => console.log(error))
    },
    getGenres: function () {
        axios.get('https://django-intro-chelseashin.c9users.io/api/v1/genres/')
            .then(res => res.data)
            .then(genres => {
                this.genres = genres
            })
    },
    addScore: function (movie) {
        axios.post(`https://django-intro-chelseashin.c9users.io/api/v1/movies/${movie.id}/scores/`, {content: this.movieDetail.newComment, score: this.movieDetail.newScore})
            .then(response => {
                this.movieDetail.scores.push({content: this.movieDetail.newComment, score: this.movieDetail.newScore}),
                this.movieDetail.newComment ='',
                this.movieDetail.newScore = 0
            })
            .catch(error => console.log(error))
        }
  },
  mounted: function (){
    this.getMovies()
    this.getGenres()
    this.addScore()
  },
    // 까지 추가
  computed: {},
  watch: {},

  created: function () {  // Vue 인스턴스가 생성되는 시점에 실행되는 함수입니다. 현재는 Vue 인스턴스가 생성되면, json-server 에서 장르목록만 받아옵니다.
      axios.get(`${HOST}/genres`)  // 만약 json-server 를 사용하지 않거나 서버가 꺼져있다면 에러가 발생합니다.
        .then(res => this.genres = res.data)
  }
});
