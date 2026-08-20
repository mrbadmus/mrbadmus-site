/* ══════════════════════════════════════════════════════════════
   GENERATED — do not edit. `python3 build_student_port.py`
   ══════════════════════════════════════════════════════════════

   Claude Design's own example data for the class view, lifted out of
   Design's logic class and out of Design's template by source
   transformation — not retyped, and not re-serialised. Every value
   below is the same bytes Design wrote.

   ⛔ FOR THE GATES ONLY. This is one real class's homework with one
   real child's name on it, frozen. It is loaded by class-fixture.html and by nothing
   that a student can reach: the production page loads student-live.js instead,
   and `MRB_DATA` throws rather than falling back to this.
   ══════════════════════════════════════════════════════════════ */
window.__MRB_DATA__ = {
  "work": [
    { id: 'a5', week: 4, title: 'Cells & microscopy', brief: '8 questions \u00B7 draws on this week\u2019s lessons', status: 'open', detail: 'SET MON 15 SEP \u00B7 8 QUESTIONS \u00B7 DUE THU 18:00' },
    { id: 'a4', week: 3, title: 'Digestion', brief: '6 questions \u00B7 enzymes and the gut', status: 'marked', score: 82, detail: 'MARKED 11 SEP \u00B7 6 OF 8 QUESTIONS RIGHT',
      notes: [
        { text: 'Questions 3 and 7 put the enzyme in the wrong part of the gut. Read the second half of the lesson before the next one.', meta: 'ON QUESTIONS 03, 07 \u00B7 11 SEP' },
        { text: 'Handed in early and the working was set out clearly. Same again this week.', meta: 'ON THE WHOLE PIECE \u00B7 11 SEP' }
      ], items: [1, 1, 0, 1, 1, 1, 0, 1] },
    { id: 'a3', week: 3, title: 'Movement & joints', brief: '5 questions \u00B7 muscles and bones', status: 'marked', score: 71, retake: true, detail: 'MARKED 9 SEP \u00B7 3 OF 5 QUESTIONS RIGHT',
      notes: [{ text: 'Two answers named the wrong bone. The retake is open until Friday and the better mark counts.', meta: 'ON QUESTIONS 02, 04 \u00B7 9 SEP' }],
      items: [1, 0, 1, 0, 1] },
    { id: 'a2', week: 2, title: 'Gas exchange', brief: '10 questions \u00B7 lungs and breathing', status: 'pending', late: true, detail: 'HANDED IN 2 DAYS LATE \u00B7 WITH MR BADMUS' },
    { id: 'a1', week: 1, title: 'Cell parts', brief: '8 questions \u00B7 starter set', status: 'marked', score: 95, detail: 'MARKED 2 SEP \u00B7 8 OF 8 QUESTIONS RIGHT',
      notes: [{ text: 'Full marks. Move on to the microscopy lesson before Thursday.', meta: 'ON THE WHOLE PIECE \u00B7 2 SEP' }], items: [1, 1, 1, 1, 1, 1, 1, 1] },
    { id: 'a0', week: 1, title: 'Lab safety check', brief: '8 questions \u00B7 before any practical', status: 'missed', detail: 'CLOSED 1 SEP \u00B7 NOT HANDED IN' }
  ],
  "roster": [
    { id: 's1', name: 'Tiwa A.', mono: 'TA' }, { id: 's2', name: 'Marcus O.', mono: 'MO' },
    { id: 's3', name: 'Ayo B.', mono: 'AY', me: true }, { id: 's4', name: 'Hafsah I.', mono: 'HI' },
    { id: 's5', name: 'Daniel K.', mono: 'DK' }, { id: 's6', name: 'Priya S.', mono: 'PS' },
    { id: 's7', name: 'Ronke E.', mono: 'RE' }, { id: 's8', name: 'Jamie L.', mono: 'JL' },
    { id: 's9', name: 'Oscar N.', mono: 'ON' }, { id: 's10', name: 'Zainab F.', mono: 'ZF' },
    { id: 's11', name: 'Ethan C.', mono: 'EC' }, { id: 's12', name: 'Mira P.', mono: 'MP' }
  ],
  "weekPts": {
    1: [72, 88, 64, 91, 55, 79, 83, 47, 68, 94, 60, 51],
    2: [95, 81, 78, 70, 66, 86, 74, 58, 90, 62, 49, 84],
    3: [84, 92, 88, 76, 71, 63, 97, 55, 67, 80, 73, 59],
    4: [98, 91, 94, 86, 74, 88, 69, 62, 80, 77, 71, 65]
  },
  "lessonDefs": [
    { num: '01', name: 'Life processes and cells', meta: 'READ \u00B7 4 RUNGS DONE' },
    { num: '02', name: 'Using a microscope', meta: 'THIS WEEK \u00B7 SET IN THE ASSIGNMENT', on: true },
    { num: '03', name: 'Animal and plant cells', meta: 'NOT OPENED' },
    { num: '04', name: 'Specialised cells', meta: 'NOT OPENED' }
  ],
  "questions": [
    { topic: 'CELLS & MICROSCOPY', a: 'B',
      q: 'An eyepiece lens of 10 and an objective lens of 40 are used together. What is the total magnification?',
      o: ['50, because the two lens powers are added together',
          '400, because the two lens powers are multiplied together',
          '40, because the objective lens does all of the magnifying',
          '4, because the objective is divided by the eyepiece'],
      f: ['Magnification multiplies at each lens. It is never added.',
          'Right. Each lens magnifies the image the next one receives, so the two powers multiply.',
          'The objective magnifies first, but the eyepiece then magnifies that image again.',
          'Nothing is divided here. Both lenses enlarge the image.'] },
    { topic: 'CELL PARTS', a: 'A',
      q: 'Which structure would you find in a plant cell but never in an animal cell?',
      o: ['A chloroplast, where light is absorbed for photosynthesis',
          'A nucleus, which holds the genetic material',
          'A mitochondrion, which releases energy from glucose',
          'A cell membrane, which controls what enters the cell'],
      f: ['Right. Animal cells cannot photosynthesise, so they have no chloroplasts.',
          'Both plant and animal cells have a nucleus.',
          'Both plant and animal cells respire, so both have mitochondria.',
          'Every cell has a membrane, plant or animal.'] },
    { topic: 'CELLS & MICROSCOPY', a: 'B',
      q: 'What is the job of the cell membrane?',
      o: ['To hold the cell in a rigid shape',
          'To control which substances enter and leave the cell',
          'To store sap and keep the cell firm',
          'To carry the instructions for making proteins'],
      f: ['That is the cell wall, and only plant cells have one.',
          'Right. The membrane is partially permeable, so some substances pass through and others do not.',
          'That is the vacuole, which sits inside the cell.',
          'That is the nucleus.'] },
    { topic: 'DIGESTION', a: 'A',
      q: 'Why does the body use enzymes to digest food?',
      o: ['They break large food molecules into small ones the body can absorb',
          'They squeeze the food along the gut a little at a time',
          'They neutralise the acid that the stomach makes',
          'They carry the digested food to the cells that need it'],
      f: ['Right. Only small molecules can pass through the wall of the small intestine.',
          'That is peristalsis, done by muscles in the gut wall.',
          'Bile does that, and bile is not an enzyme.',
          'The blood does that, after absorption.'] },
    { topic: 'MOVEMENT & JOINTS', a: 'B',
      q: 'Why do muscles have to work in pairs across a joint?',
      o: ['One muscle is stronger, so the weaker one helps it',
          'A muscle can only pull, so a second muscle pulls the bone back',
          'Two muscles contracting together can lift twice the weight',
          'Each muscle is joined to a different bone, so both must move'],
      f: ['Strength is not the reason. Think about what a muscle can and cannot do.',
          'Right. Muscles pull but never push, so an antagonistic pair moves the bone both ways.',
          'In a pair, one contracts while the other relaxes. They do not contract together.',
          'Both muscles of a pair cross the same joint.'] },
    { topic: 'GAS EXCHANGE', a: 'B',
      q: 'Alveoli are covered in a dense network of capillaries. Why does that matter?',
      o: ['It keeps the air inside the lungs warm',
          'It gives oxygen a very short distance to diffuse into the blood',
          'It pushes the air back out when you breathe out',
          'It lets the blood carry whole bubbles of air to the muscles'],
      f: ['Air is warmed in the nose and airways, and that is not what the capillaries are for.',
          'Right. A short diffusion distance and a large surface area together make gas exchange fast.',
          'The diaphragm and the ribs do that.',
          'Only dissolved gases cross into the blood, never bubbles.'] }
  ],
  "streak": 3,
  "className": "8r/Sc1",
  "classNamePadded": "8r/Sc1\n        ",
  "classSize": "28 students",
  "studentFirstName": "Ayo",
  "studentInitials": "AY",
  "subjectLabel": "Biology",
  "teacherInitials": "MB",
  "teacherName": "Mr Badmus",
  "termLabel": "AUTUMN TERM",
  "topicTitle": "Cells & microscopy",
  "welcomeLine": "Welcome back, Ayo \u00b7 your class"
};
