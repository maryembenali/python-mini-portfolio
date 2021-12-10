#SQL
#-- Q1 :
2 -- a :
3 select name
4 from country
5 where population > 10000000
6 order by name
7
8 -- b :
9 select name
10 from country
11 order by area asc
12 limit 10
13
14 -- c :
15 update country
16 set population = 11530000
17 where code = 'TN'
18
19 -- c : augmenter la population de la tunisie de 5 %
20 update country
21 set population = 1.05*population
22 where code = 'TN'
23
24 -- d :
25 insert into country (name , code , capital)
26 values ( 'soudan du sud' , 'RSS' , 'Djouba')
27 -- e :
28 DELETE
29 FROM country
30 where capital is NULL
31
32 -- Q2 :
33 create table encompasses (
34 country TEXT ,
35 continent TEXT ,
36 percentage REAL NOT NULL ,
37 primary key(country, continent),
38 foreign key(country) references country(code)
39 )
40
41 -- Q3 :
42 -- a :
43 -- avec sous requetes
44 select name
45 from country
46 where code IN ( select distinct country
47 from encompasses
48 where percentage < 100
49 )
50 -- avec jointure :
51 select C.name
52 from country C
53 join encompasses E
54 on C.code = E.country
55 where E.percentage < 100
56
57 -- b :
58 select name
59 from country
60 where population/area < 10
61 AND code IN ( select country
62 from encompasses
63 where continent like '_meri%'
64 )
65 -- avec jointure :
66 select name
67 from country C
68 join encompasses E
69 on C.code = E.country
70 where E.continent = 'America'
71 AND C.population / C.area < 10
72
73

74
75 -- Q : donner le continent de la capitale Budapest ?
76 select continent
77 from encompasses
78 where country = ( select code
79 from country
80 where capital = 'Budapest')
81
82 -- Q : donner la liste des capitales du meme continent
83 -- que celle de Budapest privé du Budapest?
84
85 select capital
86 from country
87 where code IN ( select country
88 from encompasses
89 where continent = ( select continent
90 from encompasses
91 where country = ( select code
92 from country
93 where capital = 'Budapest')
94 )
95 )
96 AND capital <> 'Budapest'
97
98 -- Fonctions SQL :
99 -- 1. count(...) : compter le nombre de lignes
100 -- 2. sum( ... ) : somme des valeurs de la colonne
101 -- 3. max(...)
102 -- 4. min (... )
103 -- 5. avg(...) : moyenne
104
105
106 select name , population/ area as density
107 from country
108 where density > ( select avg(popuation / area )
109 from country
110 )
111
112 -- le nom du pays ayant la densite min ?
113 select name, population / area
114 from country
115 where population / area = (select min(population/area)
116 from country )
117 -- ou bien :
118 select name, population / area as densite
119 from country
120 order by densite asc
121 limit 1
122
123 -- le nombre des pays africaines ?
124 select count(*)
125 from encompasses
126 where continent = 'Africa'
127 -- count(*) : nb ligne
128 -- count(col1) : nb de valeur dans la colonne col1 <> Null
129 -- count(distinct col1) : nb de valeur different de colonne col1
130
131 -- la population de l'afrique ?
132
133 select sum(population)
134 from country
135 where code IN (select country
136 from encompasses
137 where continent = 'Africa'
138 )
139
140 -- La jointure :
141 select *
142 from country
143 join encompasses
144 on country.code = encompasses.country
145 -- ou bien :
146 select *

147 from country C
148 join encompasses E
149 on C.code = E.country
150 -- ou bien
151 select *
152 from country C , encompasses E
153 where C.code = E.country
154
155
156 -- La liste des noms des pays et leurs contienent qui ont une densite < 10
157 -- avec jointure :
158 select C.name , E.continent
159 from country C
160 join encompasses E
161 on C.code = E.country
162 where C.popuation / C.area < 10
163
164 -- avec sous requetes : impossible : projection sur deux colonnes de deux tables
differents
165 select name , continent
166 from ????
167
168 --- la popuation mondiale privé du continent Asia
169 select sum(population)
170 from country C
171 join encompasses E
172 on C.code = E.country
173 where continent <> 'Asia'
174 -- ou bien :
175 select sum(population)
176 from country
177 where code not in (select country
178 from encompasses
179 where continent = 'Asia'
180 )
181 -- ou bien
182 select sum(population )
183 from country
184 where code IN ( select code
185 from country
186 except
187 select country
188 from encompasses
189 where continent = 'asia'
190 )
191
192 -- c :
193 select continent , sum(population) as S
194 from country C
195 join encompasses E
196 ON C.code = E.country
197 group by E.continent
198 having S > 1000000000
199
200
201 -- d :
202 select name
203 from country
204 where population / area > ( select avg(population / area )
205 from country
206 )
207
208 -- Q4 :
209 -- a :
210 select name , count(*) as N
211 from language
212 group by name
213 order by N desc
214 limit 10
215
216 -- b :
217 -- i :
218 select name

219 from language
220 group by name
221 having count(*) = 6
222
223 -- ii :
224 select name
225 from country
226 where code in ( select country
227 from language
228 where name in (select name
229 from language
230 group by name
231 having count(*) = 6
232 )
233 )
234 -- ou bien :
235 select C.name
236 from country C
237 join language L
238 on C.code = L.country
239 where L.name in in (select name
240 from language
241 group by name
242 having count(*) = 6
243 )
244
245 -- Q : la liste des noms des pays et leurs continent parlant l'arabe ?
246 select name , continent
247 from ???
248 -- avec jointure
249 select C.name , E.continent
250 from country C
251 join encompasses E
252 on C.code = E.country
253 join language L
254 on L.country = C.code
255 where L.name = 'Arabic'
256
257 -- c :
258 select L.name , sum(population * L.percentage / 100) as P
259 from country C
260 join language L
261 on C.code = L.country
262 group by L.name
263 having P < 30000
264
265 -- d : la langue dominante dans l'afrique
266
267 select L.name , sum(population * L.percentage / 100) as P
268 from country C
269 join language L
270 on C.code = L.country
271 join encompasses E
272 on E.country = C.code
273 where E.continent = 'Africa'
274 group by L.name
275 order by P desc
276 limit 5
277
278 -- Algebre :
279 -- a :
280 select name
281 from city
282 where latitude > 66
283 INTERSECT
284 select name
285 from city
286 where population > 10000
287 --> la liste des noms des villes ayant une latitude sup a 66
288 -- et une population qui excede 10000
289 -- Q : donner la ville europeene situé à une latitude max.
290 select T.name
291 from city T

292 join encompasses E
293 on T.country = E.country
294 where E.continent = 'Europe'
295 order by T.latitude desc
296 limit 1
297
298 select T.name
299 from city T
300 join encompasses E
301 on T.country = E.country
302 where E.continent = 'Europe'
303 AND T.latitude = ( select max(latitude)
304 from city T
305 join encompasses E
306 on T.country = E.country
307 where E.continent = 'Europe'
308 )
309 -- b :
310 select C.name
311 from country C
312 join city T
313 ON C.code = T.country
314 where T.latitude > -23
315
316 -- > la liste des noms des pays ayant des villes situé a une latitude sup -23
317
318
319 -- c :
320 select T.name
321 from country C
322 join encompasses E
323 on C.code = E.country
324 join city T
325 ON T.country = C.code
326 where E.continent = 'Europe'
327 AND T.latitude > 60
328 AND C.capital = T.name