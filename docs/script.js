document.addEventListener("DOMContentLoaded", () => {

    /* Smooth reveal animation */
    const cards = document.querySelectorAll(
        ".stat-card, .progress-card, .topic-card, .solution-card"
    );

    const observer = new IntersectionObserver(
        (entries) => {

            entries.forEach((entry) => {

                if (entry.isIntersecting) {

                    entry.target.style.opacity = "1";
                    entry.target.style.transform = "translateY(0)";

                    observer.unobserve(entry.target);
                }

            });

        },
        {
            threshold: 0.12
        }
    );


    cards.forEach((card) => {

        card.style.opacity = "0";
        card.style.transform = "translateY(20px)";
        card.style.transition = "opacity 0.6s ease, transform 0.6s ease";

        observer.observe(card);

    });


    /* Progress bar animation */
    const progressBars = document.querySelectorAll(".progress-fill");

    progressBars.forEach((bar) => {

        const finalWidth = bar.style.width;

        bar.style.width = "0";

        setTimeout(() => {
            bar.style.width = finalWidth;
        }, 250);

    });


    /* Active navigation */
    const sections = document.querySelectorAll("section[id]");
    const navigationLinks = document.querySelectorAll(".nav-links a");

    window.addEventListener("scroll", () => {

        let current = "";

        sections.forEach((section) => {

            const sectionTop = section.offsetTop - 120;

            if (window.scrollY >= sectionTop) {
                current = section.getAttribute("id");
            }

        });

        navigationLinks.forEach((link) => {

            link.classList.remove("active");

            if (link.getAttribute("href") === `#${current}`) {
                link.classList.add("active");
            }

        });

    });

});
